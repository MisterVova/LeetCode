# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
from random import random
from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        node = root
        steck: List[Tuple[int, TreeNode]] = []
        h = 0
        while node:
            node_next = None
            if h >= len(ret):
                ret.append(node.val)

            if node.left is not None:
                steck.append((h + 0, node.left))

            if node.right is not None:
                node_next = node.right

            if (node_next is None) & (len(steck) != 0):
                h, node_next = steck.pop()

            h = h + 1
            node = node_next

        return ret

    def rightSideView_v0(self, root: Optional[TreeNode]) -> List[int]:
        ret: List[int] = []
        self.add_value(ret, root, 0)
        return ret

    def add_value(self, ret: List[int], node: Optional[TreeNode], h):
        if node is None: return
        if h >= len(ret):
            ret.append(node.val)
        else:
            ret[h] = node.val
        self.add_value(ret, node.left, h + 1)
        self.add_value(ret, node.right, h + 1)


def make_tree(lst=List[int]) -> Optional[TreeNode]:
    lst_node = [TreeNode(val) for val in lst]
    # print(lst_node)
    # nodes_bif: List[TreeNode] = list()

    nodes_current: List[TreeNode] = list()

    nodes_next: List[TreeNode] = list()

    if len(lst_node) == 0:
        return None

    if lst_node[0].val is None:
        return None

    rt = lst_node[0]
    nodes_current.append(rt)

    i = 1
    while i < len(lst_node):
        for nod in nodes_current:
            if i < len(lst_node):
                if lst_node[i].val is not None:
                    nod.left = lst_node[i]
                    nodes_next.append(nod.left)
            i = i + 1
            if i < len(lst_node):
                if lst_node[i].val is not None:
                    nod.right = lst_node[i]
                    nodes_next.append(nod.right)
            i = i + 1
        if i >= len(lst):
            break
        if len(nodes_next) == 0:
            break
        # nodes_next
        nodes_current = nodes_next
        nodes_next = list()

    return rt


def make_tree_v1(rt: TreeNode, lst=List[int]) -> Optional[TreeNode]:
    nodes_bif: List[TreeNode] = list()

    nodes_current: List[TreeNode] = list()

    nodes_next: List[TreeNode] = list()

    nodes_current.append(rt)

    # lst.reverse()
    i = 0
    # while len(lst):
    while i < len(lst):
        for nod in nodes_current:
            if i < len(lst):
                nod.val = lst[i]
            i = i + 1

        if i >= len(lst):
            break

        for nod in nodes_current:
            if nod.val is not None:
                nod.left = TreeNode(None)
                nod.right = TreeNode(None)
                nodes_next.append(nod.left)
                nodes_next.append(nod.right)

        nodes_current = nodes_next
        nodes_next = list()

    return rt


if __name__ == '__main__':
    from datetime import datetime

    start_time = datetime.now()
    null = None
    tests = [
                {"Expected": [1, 3, 4], "Output": None, "Input": [1, 2, 3, null, 5, null, 4], "rt": None, },
                {"Expected": [1, 3], "Output": None, "Input": [1, null, 3], "rt": None, },
                {"Expected": [], "Output": None, "Input": [], "rt": None, },
                {"Expected": [1, 2, 2, 5], "Output": None, "Input": [1, 2, null, 1, 2, 3, 4, 5], "rt": None, },
                {"Expected": [1, 2, 2, 4], "Output": None, "Input": [1, null, 2, 1, 2, 3, 4], "rt": None, },
                {"Expected": [1, 2], "Output": None, "Input": [1, 2], "rt": None, },
                {"Expected": [], "Output": None, "Input": [4, 1, 5, null, 2, null, 6, null, 3], "rt": None, },
                {"Expected": [1, 3, 5], "Output": None, "Input": [1, 2, 3, null, 5, null, null], "rt": None, },
                {"Expected": [1, 2], "Output": None, "Input": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, ], "rt": None, },
            ] + [
                 {"Expected": [], "Output": None, "Input": [0] + [None if random() < 0.5 else i+2 for i in range(2 ** 6 - 1)], "rt": None, } for j in range(10)
            ]

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
    print("ok 1")
    for test in tests:
        # print(test["Input"])
        # root = TreeNode(None)
        test["rt"] = make_tree(test.get("Input", []))
        # print(rt.val)

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
    print("ok 2")
    for test in tests:
        solution = Solution()
        test["Output"] = v1 = solution.rightSideView(test["rt"])
        v0 = solution.rightSideView_v0(test["rt"])
        # v0 = []
        # print("!!" if v1 != v0 else "ok", test)
        if v1 != v0:
            print("!!" if v1 != v0 else "ok", v1, v0, test["Input"], sep="\n")

    print("ok 6")
    # if test["Output"] != test["Expected"]:
    #     print("!!", test)
    # else:
    #     print("ok", test)

    # solution = Solution()
    #
    #
    #
    # start_time = datetime.now()
    # for test in tests:
    #     test["Output_vO"] = solution.rightSideView_v0(test["rt"])
    # end_time = datetime.now()
    # print('Duration: {}'.format(end_time - start_time))
    # print("ok 4")
    #
    # start_time = datetime.now()
    # for test in tests:
    #     test["Output"] = v1 = solution.rightSideView(test["rt"])
    #     v0 = solution.rightSideView_v0(test["rt"])
    # end_time = datetime.now()
    # print('Duration: {}'.format(end_time - start_time))
    # print("ok 3")
