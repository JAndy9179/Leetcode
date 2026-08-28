"""
思路:

想要爬到 n 阶时, 有两种情况:
    1. 从 n - 1 阶迈一步到 n 阶
    2. 从 n - 2 阶迈两步到 n 阶
因此状态 dp[n] = dp[n - 1] + dp[n - 2]
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0 for _ in range(n)]
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n - 1]
