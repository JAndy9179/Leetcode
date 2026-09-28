"""
思路: 中序遍历

二叉树中序遍历后的结果如果是严格升序, 则二叉树满足二叉搜索树, 即节点的左子树只包含严格小于该节点的值数, 节点的右子树只包含严格大于该节点的值数
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        s = []

        def bst(node):
            if not node:
                return
            
            bst(node.left)
            s.append(node.val)
            bst(node.right)

        bst(root)
        for i in range(len(s) - 1):
            if s[i] >= s[i + 1]:
                return False

        return True
