import os
import json
from typing import Dict, List, Tuple

few_shot_example = "Here are some examples. [GOAL] the orange block is on top of the white block and the yellow block is on top of the red block\n[STATE 0] I have that, the red block is clear, the yellow block is clear, the white block is clear, the hand is empty, the orange block is on top of the blue block, the yellow block is on top of the orange block, the red block is on the table, the blue block is on the table and the white block is on the table.\n[ACTION] Unstack the yellow block from on top of the orange block.\n[Possibility] Sure.\n[GOAL] the orange block is on top of the white block and the yellow block is on top of the red block\n[STATE 0] I have that, the red block is clear, the yellow block is clear, the white block is clear, the hand is empty, the orange block is on top of the blue block, the yellow block is on top of the orange block, the red block is on the table, the blue block is on the table and the white block is on the table.\n[ACTION] Pick up the white block.\n[Possibility] Impossible.\n"

value_prompt = "Now given the goal and state:{}\n{}\nEvaluate how possible you take the action: \"{}\". Don't provide any additional commentary and don't include any explanations in your responses. Answer in a single word (sure/maybe/impossible)."


class TotAgent:
    def __init__(self, args, specialist) -> None:
        self.specialist = specialist
        self.breadth = args.bfs_breadth

    def evaluate_actions(self, node) -> Dict[str, int]:
        node.generate_children()
        d = {}
        for action in node.action_space:
            # try for three times
            for _ in range(3):
                prompt = few_shot_example
                prompt += value_prompt.format("[GOAL] " + node.goal_statement,
                                              "[STATE {}] ".format(node.depth) + node.self_state,
                                              action)
                conversation = [
                    {"role": "system", "content": "You are an evaluator on the action possibility in the Blocks World planning task."},
                    {"role": "user", "content": prompt}
                ]
                response = self.specialist(conversation).lower()
                print(conversation)
                print(response)
                if 'sure' in response:
                    d[action] = 2
                    break
                elif 'maybe' in response:
                    d[action] = 1
                elif 'impossible' in response:
                    d[action] = 0
                else:
                    raise ValueError("Can't get action possibility")
        return d

    def get_action(self, node) -> str:
        '''Estimate the best action'''
        # do value iteration first
        value_dict = self.evaluate_actions(node)
        # return the action with max state-action value
        return max(value_dict, key=value_dict.get) # method 1
        # sorted_items = sorted(value_dict.items(), key=lambda x: x[1], reverse=True) # method 2
        # return sorted_items[:self.breadth]

    def update_memory(self, root_node, end_node, trajectory: str, action_option_history: List[List[str]]) -> Tuple[None, None, None]:
        return None, None, None

    def update_goal_memory(self, trajectory: str) -> None:
        pass

    def snapshot(self, log_folder_path: str, run_prefix: str, conversation: List[Dict]):
        pass
