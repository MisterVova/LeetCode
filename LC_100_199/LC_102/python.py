# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
from random import random
from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret: List[List[int]] = []
        nodes_current: List[TreeNode] = list()
        nodes_next: List[TreeNode] = list()

        if root is not None:
            nodes_current.append(root)

        while len(nodes_current):
            vls: List[int] = list()
            for node in nodes_current:
                vls.append(node.val)
                if node.left:
                    nodes_next.append(node.left)
                if node.right:
                    nodes_next.append(node.right)
            if len(vls):
                ret.append(vls)
            nodes_current = nodes_next
            nodes_next: List[TreeNode] = list()

        return ret


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


if __name__ == '__main__':
    from datetime import datetime

    start_time = datetime.now()
    null = None
    tests = [
                {"Expected": [1, 3, 5], "Output": None, "Input": [3, 9, 20, null, null, 15, 7], "rt": None, },
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
                {"Expected": [], "Output": None, "Input": [0] + [None if random() < 0.3 else i + 2 for i in range(2 ** 6 - 1)], "rt": None, } for j in range(10)
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

        v1 = solution.levelOrder(test["rt"])
        # test["Output"] = v1 = solution.rightSideView(test["rt"])
        # v0 = solution.rightSideView_v0(test["rt"])
        # v0 = []
        print(v1, test["Input"], "", sep="\n")
        # print("!!" if v1 != v0 else "ok", test)
        # if v1 != v0:
        #     print("!!" if v1 != v0 else "ok", v1, v0, test["Input"], sep="\n")

    print("ok FINISH")
