import re
import torch
from typing import Union


def extract_color(s: str) -> Union[str, None]:
    match = re.search(r'the (\w+) block', s)
    if match:
        return match.group(1)
    return None


def extract_block(s: str) -> str:
    return "the {} block".format(
        extract_color(s)
    )


def extract_topper(target: str, state: str) -> str:
    match = re.search(r'the (\w+) block is on top of ' + target, state)
    return "the {} block".format(
        match.group(1)
    )


def count_obstacles(target: str, state: str) -> int:
    cnt = 0
    while True:
        if target + " is clear" in state:
            return cnt
        cnt += 1
        target = extract_topper(target, state)


def generate_all_actions(state):
    return_list = []
    if "hand is empty" in state:
        block = re.findall("the [a-z]{0,10} block is clear", state)
        block_color = [re.search("the ([a-z]{0,10}) block is clear", b).group(1) for b in block]
        # print(block_color)
        for c in block_color:
            # print("looking for", c)
            if f"the {c} block is on the table" in state:
                return_list.append(f"Pick up the {c} block")
            else:
                c_ = re.search(f"the {c} block" + " is on top of the ([a-z]{0,10}) block", state).group(1)
                return_list.append(f"Unstack the {c} block from on top of the {c_} block")
    else:
        c = re.search("is holding the ([a-z]{0,10}) block", state).group(1)
        block = re.findall("the [a-z]{0,10} block is clear", state)
        clear_color = [re.search("the ([a-z]{0,10}) block is clear", b).group(1) for b in block]
        for c_ in clear_color:
            return_list.append(f"Stack the {c} block on top of the {c_} block")
        return_list.append(f"Put down the {c} block")
    return return_list


def apply_change(change, state):
    # print("input state:", state)
    if "and the " in state and ", and the" not in state:
        state = state.replace("and the ", ", and the ")
    states = state.split(", ")
    states = [s.strip()[4:].strip(".") if s.strip().startswith("and ") else s.strip().strip(".") for s in states]
    # print("state", states)

    changes = change.lower().strip().strip(".").split(", ")
    # print("initial states:", states)
    for c in changes:
        if c.startswith("and "):
            c = c[4:]
        success = 0
        # print("current change", c)
        if c.startswith("the hand"):
            # 防止llm重复说话
            if "and" not in c or "was" not in c or "now" not in c:
                continue
            # print(c)
            old = c.split("was")[1].split("and")[0].strip()
            # print(old)
            new = c.split("now")[1].strip()
            # print(new)
            for idx in range(len(states)):
                # print("=", s)
                if ("hand is " + old) in states[idx]:
                    # print(":", s)
                    states[idx] = states[idx].replace(old, new)
                    success += 1
                    # print(s)
        else:
            
            colors = re.findall(r"the (\w+) block", c)
            if len(colors) == 0:
                print("Error: zero-colors")
                print(c)
                torch.distributed.barrier()
                raise Exception("ERROR")
            color = colors[0]
            # print(colors)
            if c.startswith(f"the {color} block"):
                # print("SUB:", f"the {color} block")
                subj = f"{color} block"
                if "no longer" in c:
                    old = c.split("no longer")[1].strip()
                    # print("old:", old)
                    for idx in range(len(states)):
                        if f"{color} block is " + old in states[idx]:
                            states[idx] = ""
                            success += 1
                elif "was" in c and "now" in c:
                    old = c.split("was")[1].split(" and")[0].strip()
                    new = c.split("now")[1].strip()
                    # print("previous:", "{color} block is " + old)
                    for idx in range(len(states)):
                        if f"{color} block is " + old in states[idx]:
                            states[idx] = states[idx].replace(old, new)
                            success += 1
                elif "now" in c:
                    new = c.split("now")[1].strip()
                    states.append("the " + color + " block is " + new)
                    success += 1
            else:
                # print("ERROR")
                print("Error: not recognized")
                torch.distributed.barrier()
                raise Exception("ERROR")
        if success == 0:
            # print("ERROR")
            print("Error: no successful change")
            print(c)
            print(states)
            torch.distributed.barrier()
            raise Exception("ERROR")
        # print("current states:", states)
    states = [s for s in states if s != ""]
    priority_states = []
    for s in states:
        if "have that" in s:
            priority_states.append(0)
        elif "clear" in s:
            priority_states.append(1)
        elif "in the hand" in s:
            priority_states.append(1)
        elif "the hand is" in s:
            priority_states.append(2)
        elif "on top of" in s:
            priority_states.append(3)
        elif "on the table" in s:
            priority_states.append(4)
        else:
            print("Error: unknown state")
            print(s)
            torch.distributed.barrier()
            raise Exception("ERROR")
    sorted_states = [x.strip() for _, x in sorted(zip(priority_states, states))]
    sorted_states[-1] = "and " + sorted_states[-1]
    return ", ".join(sorted_states) + "."


def get_world_change(last_state, last_action):

    '''  solve the hand state. note that the sentence could end with "." or ","  '''
    hand_pattern = r"(the hand is .*?[,\.])"
    # find the last description of hand status
    hand_last_state = re.findall(hand_pattern, last_state)[0][:-1]
    # replace "is" with "was" for the world_change format
    hand_last_state_past_tense = hand_last_state.replace('is', 'was')
    # turn the string into a list to change "the" to "The"
    hand_last_state_past_tense = list(hand_last_state_past_tense)
    hand_last_state_past_tense[0] = 'T'
    hand_last_state_past_tense = "".join(hand_last_state_past_tense)

    '''  solve the manipulated block state. note that the sentence could end with "." or ","  '''
    block_info_index1 = last_action.index('the')
    block_info_index2 = last_action.index('block')
    block_info = last_action[block_info_index1:block_info_index2+6]
    # remove the ending spaces and '.'
    block_info = block_info.replace('.', '')
    block_info = block_info.rstrip()
    block_pattern = r"(" + block_info + r" is .*?[,\.])"
    block_last_state = re.findall(block_pattern, last_state)[0][:-1]
    # replace "is" with "was" for the world_change format
    block_last_state_past_tense = block_last_state.replace('is', 'was')

    if "Pick" in last_action: 
        hand_change = hand_last_state_past_tense + ' and is now holding ' + block_info
        block_change = block_info + ' was on the table and is now in the hand'
        table_change = 'and ' + block_info + ' is no longer clear'
    elif "Unstack" in last_action:
        hand_change = hand_last_state_past_tense + ' and is now holding ' + block_info
        '''  solve the table related state'''
        holder_info_index1 = last_action.index('on top of the ')
        holder_info = last_action[holder_info_index1+10:]
        holder_info_index2 = holder_info.index('block')
        holder_info = holder_info[:holder_info_index2+6]
        # remove the ending spaces and '.'
        holder_info = holder_info.replace('.', '')
        holder_info = holder_info.rstrip()
        block_change = block_info + ' was on top of ' + holder_info + ' and is now in the hand, ' + block_info + ' is no longer clear'
        table_change = holder_info + ' is now clear'
    elif "Put" in last_action:
        hand_change = hand_last_state_past_tense + ' and is now empty'
        block_change = block_last_state_past_tense + ' and is now on the table'
        table_change = 'and ' + block_info + ' is now clear'
    elif "Stack" in last_action: 
        hand_change = hand_last_state_past_tense + ' and is now empty'
        '''  solve the table related state'''
        holder_info_index1 = last_action.index('on top of the ')
        holder_info = last_action[holder_info_index1+10:]
        holder_info_index2 = holder_info.index('block')
        holder_info = holder_info[:holder_info_index2+6]
        # remove the ending spaces and '.'
        holder_info = holder_info.replace('.', '')
        holder_info = holder_info.rstrip()
        block_change = block_last_state_past_tense + ' and is now on top of ' + holder_info + ', ' + holder_info + ' is no longer clear'
        table_change = 'and ' + block_info + ' is now clear'

    return hand_change + ', ' + block_change + ', ' + table_change + '.'
