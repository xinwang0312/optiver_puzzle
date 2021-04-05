"""
Author: Xin Wang
Email: xinwang0312@gmail.com
Date: Apr, 05, 2021
"""


import numpy as np
import argparse
from anytree import RenderTree, AnyNode


def cal_win_prob(numbers: list) -> np.array:
    """
    Given a list of selected numbers, calculated the winning probabilities of the corresponding
    players
    :param numbers: Numbers selected by the players
    :return: the winning probabilities of the corresponding players
    """
    sorted_indices = np.argsort(numbers)
    sorted_numbers = np.sort(numbers)
    mid = np.insert(0.5 * (sorted_numbers[:-1] + sorted_numbers[1:]), [0, len(numbers) - 1], [0, 1])
    sorted_prob = mid[1:] - mid[:-1]
    # put the winning prob in the same order as the input numbers
    win_prob = sorted_prob[np.argsort(sorted_indices)]
    return win_prob


def build_tree(numbers: np.array) -> AnyNode:
    """
    Build a game tree for the four players given a list of candidate numbers
    :param numbers: a list of candidate numbers
    :return: the root of the game tree
    """
    if min(numbers) < 0 or max(numbers) > 1:
        raise ValueError('The candidate numbers should be between 0 and 1!')
    print('Building the game tree...')
    root = AnyNode(children=[
        AnyNode(a=a, win_prob=None, children=[
            AnyNode(a=a, b=b, win_prob=None, children=[
                AnyNode(a=a, b=b, c=c, win_prob=None, children=[
                    AnyNode(a=a, b=b, c=c, d=d, win_prob=cal_win_prob([a, b, c, d]))
                    for d in numbers if d not in [a, b, c]
                ]) for c in numbers if c not in [a, b]
            ]) for b in numbers if b != a
        ]) for a in numbers if a <= 0.5
    ])
    return root


def prune_tree(parent: AnyNode, player_id: int, eps: float = 1e-8) -> None:
    """
    Given a game tree, select the optimal choice(s) for a certain player. Note that the eps arg is
    used to get rid of the numpy eps error, which will make the code more robust. For example,
    instead of 0.325, cal_win_prob([0, 0.65, 0.2])[2] is 0.32500000000000007, which will result in
    a but in pruning the tree.
    :param parent: The root of the (sub)-tree that is going to be pruned
    :param player_id: The id of the player
    :param eps: The criterion of "optimal enough".
    :return: Since all manipulations will be in-place, return nothing.
    """
    player_win_prob = [leaf.win_prob[player_id] for leaf in parent.children]
    max_ind = np.argwhere(player_win_prob >= max(player_win_prob) * (1 - eps)).ravel()
    # if there are more than 1 optimum, use the expectation
    expected_parent_win_prob = np.vstack(
        tuple(parent.children[i].win_prob for i in max_ind)
    ).mean(axis=0)
    parent.win_prob = expected_parent_win_prob
    parent.children = tuple(parent.children[i] for i in max_ind)
    return None


def solve_puzzle(n: int = 30, eps: float = 1e-8) -> AnyNode:
    """
    Solve the optiver puzzle
    :param n: We will divide interval [0, 1] into n equal length sub-intervals
    :param eps: The criterion of "optimal enough" .If the value of a node is larger than / equal
    to (1 - eps) * maximum, then the node is also considered as one of the optimal choices.
    :return: the optimal game tree
    """
    print(f'Start to solve the puzzle with n = {n}...')
    numbers = np.linspace(0, 1, n + 1)
    root = build_tree(numbers)
    print('Optimizing the strategy of D...')
    for i in range(len(root.children)):
        for j in range(n):
            for k in range(n - 1):
                prune_tree(root.children[i].children[j].children[k], 3, eps=eps)
    print('Optimizing the strategy of C...')
    for i in range(len(root.children)):
        for j in range(n):
            prune_tree(root.children[i].children[j], 2, eps=eps)
    print('Optimizing the strategy of B...')
    for i in range(len(root.children)):
        prune_tree(root.children[i], 1, eps=eps)
    print('Optimizing the strategy of A...')
    prune_tree(root, 0, eps=eps)
    print('The optimal game tree is')
    print(RenderTree(root))
    return root


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Optiver puzzle solver')
    parser.add_argument('--n', type=int, default=30, help='The number of the [0, 1] discretization')
    parser.add_argument('--eps', type=float, default=1e-8, help='The criterion of "optimal enough"')
    args = parser.parse_args()
    solve_puzzle(args.n, args.eps)
