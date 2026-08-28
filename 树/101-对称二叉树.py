"""
思路:

对于当前节点的左右子树, 左子树往左走时右子树往右, 左子树往右时右子树往左, 只有这两条路径完全镜像的时候才算对称
即: check(l.left, r.right) and check(l.right, r.left)

当存在以下不对齐的情况时返回 False:
    1. 左右子树的根节点一个为空一个不为空
    2. 左右子树的根节点值不相等
当左右子树的根节点都是 None 的时候说明都到头了, 返回 True
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(l, r):
            if l == None and r == None:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            return check(l.left, r.right) and check(l.right, r.left)

        return check(root.left, root.right)