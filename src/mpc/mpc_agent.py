import os
import re
import json
import time
import openai
import difflib
import traceback
import numpy as np
from collections import OrderedDict
from typing import Tuple, List, Dict, Optional
import colorama
from colorama import Fore
from colorama import Style
colorama.init()


def extract_integers_from_string(s) -> List[int]:
    # Use regex to find all integers in the string
    integers = re.findall(r'\d+', s)
    
    # Convert the extracted strings to integers
    return [int(i) for i in integers]


def extract_first_float(input_string) -> float:
    pattern = r'\d+\.\d+'  # Regular expression pattern for matching float numbers
    match = re.search(pattern, input_string)
    if match:
        return float(match.group())
    else:
        raise ValueError("Failed to extract float numbers from language model response.")


def extract_first_float_with_index(input_string) -> Tuple[int, float]:
    # Use regex to find all float numbers in the string
    matches = re.finditer(r"[-+]?\d*\.\d+|\d+", input_string)
    # Get the first match
    for match in matches:
        return match.end(), float(match.group())
    raise ValueError("Failed to extract float numbers from language model response.")


def extract_best_match(target, s):
    # Tokenize the large string based on some meaningful delimiters
    tokens = [token.strip() for token in s.split(",")]
    best_match = None
    best_ratio = 0
    for token in tokens:
        ratio = difflib.SequenceMatcher(None, target, token).ratio()
        if ratio > best_ratio:
            best_match = token
            best_ratio = ratio
    return best_match


class ModelPredictiveControlAgent:
    def __init__(self, args, specialist) -> None:
        self.specialist = specialist
        self.search_depth: int = args.search_depth
        self.theta: float = args.theta
        self._memory: Optional[str] = None
        # if use estimated goal accountant or not
        self.estimate_goal = args.estimate_goal
        if self.estimate_goal:
            self._goal_memory: Optional[str] = None

    def update_memory(self, root_node, end_node, trajectory: str, action_option_history: List[List[str]]) -> Tuple[List[Dict], List[str], np.ndarray]:
        print(f'{Fore.GREEN}trajectory{Style.RESET_ALL}', trajectory) # TODO:
        full_action_list = []
        for action_space in action_option_history: full_action_list += action_space
        print(f'{Fore.GREEN}full_action_list{Style.RESET_ALL}', full_action_list) # TODO:
        # first let the language model analyze in text
        conversation = [
            {"role": "system", "content": "You are a critic on the action probabilities in the Blocks World planning task. Here the history of a past experience of this task. Please critique the probability values you gave one by one."},
            {"role": "user", "content": trajectory}
        ]
        # text_analysis = self.specialist(conversation) # DEBUG
        # print(f'{Fore.GREEN}text analysis{Style.RESET_ALL}', text_analysis) # DEBUG
        # second let the language model provide the new values
        # conversation += [
        #     {"role": "assistant", "content": text_analysis},
        #     {"role": "user", "content": "Give new values for the probabilities as float numbers one by one in a single JSON array based on your critic. You should give new values for. Don't provide any additional commentary and don't include any explanations in your responses."}
        # ]  # DEBUG
        # try three times
        actions: List[str] = []
        probs: List[List] = []
        for attempt in range(3):
            try:
                # response = self.specialist(conversation)  # DEBUG
                # print(f'{Fore.GREEN}response (updated prob)|||{Style.RESET_ALL}', response) # TODO:  # DEBUG
                for action in full_action_list:
                    # method 1: extract the numbers in order
                    # ind, pr = extract_first_float_with_index(response)  # DEBUG
                    actions.append(action)
                    probs.append(1)
                    # probs.append(pr) # DEBUG
                    # response = response[ind:]  # DEBUG
                    # method 2: extract the numbers in action sequence. The order is actually the same as method 1.
                    # fuzz_action = extract_best_match(action, response)
                    # response = response.split(fuzz_action)[1]
                    # probs.append(
                    #     [action, extract_first_float(response)]
                    # )
                # set down memory
                # self._memory = text_analysis.strip("\n") # DEBUG
                return conversation, actions, np.array(probs)
            except Exception:
                print(traceback.format_exc())
                time.sleep(3)
        raise Exception("Failed to get prob value after multiple attempts.")

    def update_goal_memory(self, trajectory: str) -> None:
        print('Update goal memory')
        # let the language model analyze in text
        conversation = [
            {"role": "system", "content": "You are a expert in the planning task called \"the Blocks World\". You are able to count the subgoals achieved given a certain state of the task. Here the history of a past experience of this task. Please critique the subgoals you counted for each state. Critique one by one. Think step by step."},
            {"role": "user", "content": trajectory}
        ]
        self._goal_memory = self.specialist(conversation)

    def get_action(self, node) -> str:
        '''Estimate the best action'''
        # do value iteration first
        self.value_iteration(node)
        # return the action with max state-action value
        return max(node.q, key=node.q.get)

    def get_probs(self, node, action_list: List[str]) -> OrderedDict:
        '''Get probability of actions from language model explicitly'''
        # prepare user prompt
        prompt = ""
        if self._memory is not None:
            prompt += "[memory] " + self._memory + "\n"
        prompt += "[goal] " + node.goal_statement + "\n"
        prompt += "[state] " + node.self_state + "\n"
        prompt += "List the probabilities that you choose to " + ", or ".join(action_list)
        prompt += " as the first action to achieve the goals as a JSON array like {\"action\": your action, \"probability\": your probability}.\n"
        prompt += "Don't provide any additional commentary and don't include any explanations in your responses."
        # create conversation
        conversation = [
            {"role": "system", "content": "You are a critic on the action probabilities in the Blocks World planning task."},
            {"role": "user", "content": prompt}
        ]
        # get response from language model
        probs = OrderedDict()
        # try three times
        for attempt in range(3):
            try:
                # response = self.specialist(conversation) # DEBUG
                # sum_prob = 0
                for action in action_list:
                    # fuzz_action = extract_best_match(action, response)  # DEBUG
                    # response = response.split(fuzz_action)[1]  # DEBUG
                    # probs[action.strip("\"")] = extract_first_float(response)  # DEBUG
                    probs[action.strip("\"")] = 1 # DEBUG
                    # sum_prob += probs[action.strip("\"")]
                # normalize the prob
                # for action in probs.keys(): probs[action] /= sum_prob
                return probs
            except (openai.error.OpenAIError) as e:
                time.sleep(3)
        raise Exception("Failed to get prob value after multiple attempts.")

    def get_goalcount(self, node) -> int:
        prompt = ""
        if self._goal_memory is not None:
            prompt += "[memory] " + self._goal_memory + "\n"
            print(f'{Fore.GREEN}Using goal memory{Style.RESET_ALL}', prompt)
        prompt += "[goal] " + node.goal_statement + "\n"
        prompt += "[state] " + node.self_state + "\n"
        prompt += "How many subgoals have we achieved in the above state? Let's break down the goal and the state. And think step by step. Also think about the prerequisites of each goal."
        # first let the language model analyze in text
        conversation = [
            {"role": "system", "content": "You are a expert in the planning task called \"the Blocks World\". You are able to count the subgoals achieved given a certain state of the task."},
            {"role": "user", "content": prompt}
        ]
        text_analysis = self.specialist(conversation)
        # second let the language model provide the new values
        conversation += [
            {"role": "assistant", "content": text_analysis},
            {"role": "user", "content": "Summarize your answer in a single integer representing the number of subgoals achieved."}
        ]
        print(f'{Fore.GREEN}Get goalcount{Style.RESET_ALL}', conversation)
        # try three times
        for attempt in range(3):
            try:
                response = self.specialist(conversation)
                print(f'{Fore.GREEN}goal response{Style.RESET_ALL}', response)
                return int(extract_integers_from_string(response)[-1])
            except (openai.error.OpenAIError) as e:
                time.sleep(3)
        raise Exception("Failed to get prob value after multiple attempts.")

    def value_iteration(self, father_node) -> Tuple[List[Dict], List[float]]:
        '''U-step forward value iteration (FVI)'''

        def route(cur_node):
            if cur_node.depth - father_node.depth >= self.search_depth or cur_node.is_leaf:
                return
            action_list = []
            for action, ind in cur_node.action_index.items():
                action_list.append("\""+action+"\"")
                child = cur_node.find_child(action)
                # recursively do value iteration
                route(child)
            # get the language-based reward
            cur_node.r = self.get_probs(cur_node, action_list)
            # calculate the state-action value
            for action, prob in cur_node.r.items():
                child = cur_node.find_child(action)
                if self.estimate_goal:
                    child.est_goal = self.get_goalcount(child)
                    vrand = self.theta * child.est_goal
                else:
                    vrand = self.theta * (child.completed_subgoals - cur_node.completed_subgoals)
                # T(s,a) = s' ==> Q(s,a) = r(s,a) + V(s') = (logprob + vrand(s')) + V(s')
                # cur_node.q[action] = np.log(prob) + vrand + child.v
                cur_node.q[action] = vrand + child.v
            # From the definition in our MPC paper, V(s) = max_a Q(s,a)
            cur_node.v = max(cur_node.q.values())

        # start recursion
        route(father_node)

    def snapshot(self, log_folder_path: str, run_prefix: str, conversation: List[Dict]):
        with open(
            os.path.join(log_folder_path, run_prefix + 'memory.json'), 'w') as f:
            json.dump(conversation, f, indent=4)