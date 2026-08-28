"""
思路:

返回左右子树的最大深度 + 1
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0

            return max(depth(node.left), depth(node.right)) + 1

        return depth(root)