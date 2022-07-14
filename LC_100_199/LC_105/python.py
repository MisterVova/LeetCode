# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

class Solution:
    symbols = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def getSumm(self, s: str, i: int, b: int) -> int:
        if i < 0:
            return 0
        c = self.symbols.get(s[i], 0)
        if b > c:
            c = -1 * c
        return c + self.getSumm(s, i - 1, c)

    def romanToInt(self, s: str) -> int:
        return self.getSumm(s, len(s) - 1, 0)
