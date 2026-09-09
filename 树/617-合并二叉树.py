from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees_1(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(node1, node2, father, direction):
            if node1 and node2:
                value = node1.val + node2.val
                n1_l, n2_l = node1.left, node2.left
                n1_r, n2_r = node1.right, node2.right
            elif node1 and not node2:
                value = node1.val
                n1_l, n2_l = node1.left, None
                n1_r, n2_r = node1.right, None
            elif not node1 and node2:
                value = node2.val
                n1_l, n2_l = None, node2.left
                n1_r, n2_r = None, node2.right
            else:
                # not node1 and not node2
                return

            node = TreeNode(value, None, None)
            if direction == 'left':
                father.left = node
            if direction == 'right':
                father.right = node

            merge(n1_l, n2_l, father=node, direction='left')
            merge(n1_r, n2_r, father=node, direction='right')

        head = TreeNode(0, None, None)
        merge(root1, root2, father=head, direction='right')
        return head.right

    def mergeTrees_2(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not t1: return t2 
        if not t2: return t1  
        t1.left = self.mergeTrees_2(t1.left, t2.left)
        t1.right = self.mergeTrees_2(t1.right, t2.right)
        t1.val += t2.val
        return t1 