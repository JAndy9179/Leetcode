class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left is None:
                curr = curr.right
                continue

            l_r = curr.left
            while l_r.right:
                l_r = l_r.right
                
            r = curr.right
            l_r.right = r
            curr.right = curr.left
            curr.left = None

            curr = curr.right