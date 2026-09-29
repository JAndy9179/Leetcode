"""
注意:

1. 一定要先 build(..., 'left'), 再 build(..., 'right'), 因为前序遍历的顺序是先根节点再左子树再右子树, 交换顺序的话会把原来属于左子树的节点拿去构建右子树
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        def select_idx(nums, target):
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
            return -1

        def build(root, pre_l, in_l, direction):
            if not pre_l or not in_l:
                return

            val = pre_l.pop(0)
            node = TreeNode(val, None, None)
            if direction == 'right':
                root.right = node
            else:
                root.left = node

            idx = select_idx(in_l, val)
            build(node, pre_l, in_l[: idx], 'left')
            build(node, pre_l, in_l[idx + 1: ], 'right')

        head = TreeNode(0, None, None)
        build(head, preorder, inorder, direction='right')
        return head.right