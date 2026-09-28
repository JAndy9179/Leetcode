"""
思路: 找规律

n = 1 时 ———— 1 种      n1
n = 2 时 ———— 2 种      n1 * n0 + n0 * n1
n = 3 时 ———— 5 种      n2 * n0 + n1 * n1 + n0 * n2
n = 4 时 ———— 14 种     n3 * n0 + n2 * n1 + n1 * n2 + n0 * n3
"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(20)]
        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]

        return dp[n]