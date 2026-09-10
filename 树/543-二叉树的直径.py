"""
思路:

二叉树节点之间的路径: 可以看作是由某个节点开始, 分别向左和向右遍历的路径拼接得到
二叉树的直径: 指树中任意两个节点之间路径的最大值, 可以理解为对于任意一个节点为根节点的子树中, 若其向左遍历的节点数和向右遍历的节点数之和最多, 则可以认为这条路径就是二叉树的直径
    (其值等于路径上的节点数 - 1)
深度优先搜索: 对于以任意节点为根节点的子树, 可以通过深度优先搜索得到左右子树的深度, 因此可以计算出两个结果:
    1. 对于当前子树来说的最大直径: l + r + 1
    2. 当前节点的深度: max(l, r) + 1

因为我们要找的是整个二叉树的直径, 所以在递归的过程中, 每个子树的根节点都需要计算一下当前子树的最大直径, 然后取最大值: max(self.ans, l + r + 1)
然后返回给上一级当前节点的深度
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 1
        def dfs(node):
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            # l + r + 1: 以当前节点 node 为根节点的子树的最大直径路径上的节点数
            self.ans = max(self.ans, l + r + 1)
            # 只用返回左右子树的最大深度 + 1, 供父节点计算最大直径的时候参考
            return max(l, r) + 1

        dfs(root)
        return self.ans - 1