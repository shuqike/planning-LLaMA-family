import math
import numpy as np
from copy import deepcopy
from typing import List, Tuple
from collections import defaultdict
from src.rafa.tree_search import AbsNode


class Mcts:
    def __init__(self) -> None:
        self.w_exp = 1
        self.Q: dict[AbsNode, float] = defaultdict(lambda : 0.)
        self.N: dict[AbsNode, int] = defaultdict(lambda : 0)
        self.M: dict[AbsNode, float] = defaultdict(lambda : -math.inf)
        self.children = dict()
        self.aggr_reward = 'mean'
        self.aggr_child = 'max'
        self.discount = 1

    def _expand(self, node: AbsNode) -> int:
        if node not in self.children:
            self.children[node] = node.get_children()

    def _uct(self, node: AbsNode, log_n_f: float):
        if self.N[node] == 0:
            return node._prob_r*node._alpha + node._v_rand + self.w_exp * math.sqrt(log_n_f)
        if self.aggr_child == 'max':
            return self.M[node] + self.w_exp * math.sqrt(log_n_f / self.N[node])
        elif self.aggr_child == 'mean':
            return self.Q[node] / self.N[node] + self.w_exp * math.sqrt(log_n_f / self.N[node])

    def _uct_select(self, node: AbsNode):
        if self.N[node] == 0:
            log_n = math.log(1)
        else:
            log_n = math.log(self.N[node])
        return max(self.children[node], key=lambda n: self._uct(n, log_n))

    def _select_prior(self, node: AbsNode):
        path = [node]
        while not node.is_terminal:
            print('sp')
            self._expand(node)
            if len(self.children[node]) == 0:
                return path
            node = self._uct_select(node)
            path.append(node)
        self._expand(node)
        return path

    def _back_propagate(self, path: list[AbsNode]):
        coeff = 1
        reward = path[-1]._v_rand
        for node in reversed(path):
            reward = reward * self.discount + node._prob_r*node._alpha
            coeff = coeff * self.discount + 1
            if self.aggr_reward == 'mean':
                c_reward = reward / coeff
            else:
                c_reward = reward
            if node not in self.N:
                self.Q[node] = c_reward
            else:
                self.Q[node] += c_reward
            self.N[node] += 1
            self.M[node] = max(self.M[node], c_reward)

    def max_mean_terminal(self, cur: AbsNode, sum=0., cnt=0):
        print('mmt')
        if cur.is_terminal:
            if cur.visited:
                return cur, (sum + cur._v_rand + cur._prob_r*cur._alpha) / (cnt + 1)
            else:
                return cur, -math.inf
        if cur not in self.children or not self.children[cur]:
            return cur, -math.inf

        return max((self.max_mean_terminal(child, sum + cur._prob_r*cur._alpha, cnt + 1) for child in self.children[cur]), key=lambda x: x[1])

    def __call__(self, father_node: AbsNode) -> Tuple[AbsNode, int]:
        '''rollout'''
        path = self._select_prior(father_node)
        self._back_propagate(path)
        next_node, _ = self.max_mean_terminal(father_node)
        return next_node
