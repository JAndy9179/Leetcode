"""
思路:

每一个元素的路径和都可以由它的上边和左边的路径求和得到, 因此就想到使用动态规划, 根据 dp[i - 1][j] 和 dp[i][j - 1] 得到 dp[i][j] 的状态


初始化: 由于机器人只能向左或向下走, 因此矩阵的第一行和第一列中各个位置就只有一条路径能够到达

更新 dp 矩阵: 对于剩余位置, 它可以从上方往下走到达, 也可以从左边往右走到达, 因此得到状态转移方程 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]