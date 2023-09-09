import os
import sys
import json
import yaml
import openai
import argparse
import traceback
from functools import partial
from src.mpc.llm import chat_with_vicuna, chat_with_gpt
from src.mpc.env.blocksworld import Blocksworld, get_problem
from src.mpc.tot_agent import TotAgent
from src.mpc.mpc_agent import ModelPredictiveControlAgent
sys.path.append("gpt-plan-benchmark/gpt_plan_test")
from utils import instance_to_text_blocksworld


def parse_args():
    args = argparse.ArgumentParser()
    args.add_argument('--backend', type=str, required=True, choices=['gpt-4', 'gpt-3.5-turbo'])
    args.add_argument('--temperature', type=float, required=True)
    args.add_argument('--top_p', type=float, required=True)
    args.add_argument('--task', type=str, required=True, choices=['step_2', 'step_4', 'step_6'])
    args.add_argument('--api_key_file', type=str, required=True)
    args.add_argument('--max_steps', type=int, required=True)
    args.add_argument('--num_trials', type=int, required=True)
    args.add_argument('--theta', type=int, required=True)
    args.add_argument('--alpha_1', type=float, required=True)
    args.add_argument('--alpha_2', type=float, required=True)
    args.add_argument('--estimate_goal', action='store_true')
    args.add_argument('--task_start_index', type=int, default=0)
    args.add_argument('--task_end_index', type=int, default=10000)
    args.add_argument('--algorithm', type=str, default='mpc', choices=['mpc', 'tot'])
    args.add_argument('--search_depth', type=int, default=2)
    args = args.parse_args()
    return args


def run(args):
    if args.algorithm == 'mpc':
        agent = ModelPredictiveControlAgent(
            args=args,
            specialist=partial(chat_with_gpt,
                               engine=args.backend,
                               temperature=args.temperature,
                               top_p=args.top_p
                               )
        )
    elif args.algorithm == 'tot':
        os.environ["OPENAI_API_KEY"] = openai.api_key
        agent = TotAgent(
            args=args,
            specialist=partial(chat_with_gpt,
                               engine=args.backend,
                               temperature=args.temperature,
                               top_p=args.top_p
                               )
        )
    else:
        raise NotImplementedError

    # make experiment folder for logs
    log_folder_path = f'./logs/blocksworld/{args.backend}_{args.algorithm}{args.task}_{args.max_steps}_{args.num_trials}_{args.search_depth}_{args.temperature}_{args.top_p}_tta{args.theta}_estg{args.estimate_goal}_start{args.task_start_index}_end{args.task_end_index}/'
    os.makedirs(os.path.dirname(log_folder_path), exist_ok=True)

    # extract task description files
    data_path = 'data/blocksworld/'+args.task+'.json'
    data_files = json.load(open(data_path, 'r'))
    n_files = len(data_files)
    with open('data/blocksworld/bw_config.yaml', 'r') as f:
        data = yaml.safe_load(f)
        domain_pddl = f'gpt-plan-benchmark/gpt_plan_test/instances/{data["domain_file"]}'
    # solve the tasks
    for task_idx in range(args.task_start_index, min(args.task_end_index, n_files)):
        instance = data_files[task_idx]
        problem = get_problem(instance[0], domain_pddl)
        # get the goal and state of a task
        initial_state, goal_statement, _ = instance_to_text_blocksworld(problem, False, data)
        # create rl env
        env = Blocksworld(
            max_steps=args.max_steps,
            alpha_1=args.alpha_1,
            alpha_2=args.alpha_2,
            initial_state=f'I have that, {initial_state}.',
            goal_statement=goal_statement
        )
        # try the task a few times
        for trial_idx in range(args.num_trials):
            # name this trail run
            run_prefix = 'task_'+str(task_idx)+'_try_'+str(trial_idx)
            # redirect all the output from system stdout to the log file
            sys.stdout = open(os.path.join(log_folder_path, run_prefix+'.log'), 'w')
            # sys.stderr = sys.stdout
            # start environment
            obs = env.reset()
            done = False
            for _ in range(10):
                try:
                    while not done:
                        action = agent.get_action(env.cur_node)
                        obs, done = env.step(action)
                    # take a snapshot of the task after the trial
                    env.snapshot(
                        log_folder_path=log_folder_path,
                        run_prefix=run_prefix
                    )
                    # stop trying if succeeded
                    if obs[-1]["status"].lower() == "success":
                        break
                    # if this trial failed and is not the last trial,
                    # update the memory (reflexion)
                    elif trial_idx != args.num_trials - 1 and agent.__class__.__name__ != 'TotAgent':
                        print('Get updates')
                        # CHECK CHECK
                        conversation, actions, new_probs = agent.update_memory(
                            root_node=env.root,
                            end_node=env.cur_node,
                            trajectory=env.wrap_traj(),
                            action_option_history=env.action_option_history
                        )
                        agent.update_goal_memory(
                            trajectory=env.wrap_goal_traj()
                        )
                        # CHECK CHECK
                        # update prob estimation
                        env.update_prob(actions, new_probs) #TODO:
                        # dump the agent memory if exists
                        agent.snapshot(
                            log_folder_path=log_folder_path,
                            run_prefix=run_prefix,
                            conversation=conversation
                        )
                    break
                except Exception:
                    print(traceback.format_exc())
            if obs[-1]["status"].lower() == "success":
                break


if __name__ == '__main__':
    args = parse_args()
    with open(args.api_key_file, 'r') as f:
        openai.api_key = f.read().strip("\n")
    run(args)