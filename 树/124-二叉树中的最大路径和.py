"""
思路:

其实整体思路和 "543. 二叉树的直径" 一样, 就是通过由某个节点开始, 分别将向左和向右遍历的路径拼接得到节点的路径, 然后遍历二叉树及所有子树的路径再取最大, 只不过具体实现上会有一些区别

1. 首先 self.max_path 初始化必须得是题目指定的最小值 -1000, 不能是 0, 因为有可能节点全是负数导致最大路径也是负的
2. 计算所有子树的返回值的时候, 需要舍弃贡献为负数的子树, 即 l = paths(node.left), r = paths(node.right). 


区别: 

计算二叉树直径: 每经过一个节点, 二叉树的长度只会增加并不会减少, 因此直接取左右子树的最大深度即可;
计算最大路径和: 节点有可能是负数, 若某个子树向上提供的路径和为负，把它接到当前路径上只会让总和变小, 因此完全可以不选择这条分支
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.max_path = -1000

        def paths(node):
            if not node:
                return 0

            l = paths(node.left)
            r = paths(node.right)

            self.max_path = max(
                self.max_path,
                l + node.val,
                r + node.val,
                node.val,
                l + r + node.val
            )
            return max(l, r, 0) + node.val

        paths(root)
        return self.max_path