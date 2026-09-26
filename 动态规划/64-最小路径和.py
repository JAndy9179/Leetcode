"""
思路:

每一个元素的路径数字最小总和都可以由它的上边和左边的路径数字和的最小值, 加上当前位置的数字得到因此就想到使用动态规划


初始化: 由于只能向左或向下走, 因此矩阵的第一行和第一列中各个位置就只有一条路径能够到达:
    第一行元素: dp[0][i] = dp[0][i - 1] + grid[0][i]
    第一列元素: dp[i][0] = dp[i - 1][0] + grid[i][0]

更新 dp 矩阵: 对于剩余位置, 它只能从左边和上边到达, 因此选择二者总和最小的, 加上当前位置的数字得到当前路径的最小数字和. 得到状态转移方程 dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
"""


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        # 1. 初始化
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        # 2. 更新
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]