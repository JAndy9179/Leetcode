"""
思路:

其实试几个矩阵就知道, 顺时针旋转 90° 就等价于先上下翻转, 再沿主对角线翻转(当然也可以先沿主对角线, 再左右反转, 也可以按别的方式, 选个简单的实现就行)
"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # 1. 先沿着上下翻转
        up, down = 0, n - 1
        while up < down:
            matrix[up], matrix[down] = matrix[down], matrix[up]
            up += 1
            down -= 1

        # 2. 再沿着主对角线翻转
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]