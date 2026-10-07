"""
思路: 动态规划

使用 dp[i] 表示 s[: i] 能否被 wordDict 表示, 其中 dp 数组的长度是 n + 1, dp[0] 表示空字符串, 空字符串可以被表示(dp[0] = True).
之后遍历 i 从 1 到 n, 即逐步判断 s[: i] 能否被表示, 最终得到 s[: n + 1] 即完整字符串能否被表示.

当判断 s[: i] 能否被 wordDict 表示时, 需要使用 j 将 s[: i] 切分为 s[: j] 和 s[j: i], 然后判断 dp[j] and s[j: i] in wordDict:
    1. dp[j]: 表示 s[: j] 能否被表示
    2. s[j: i] in wordDict: 表示s[j: i] 能否被表示
遍历过程中, 一旦二者同时成立, 则说明 s[: i] 可以被 wordDict 表示, 直接更新 dp[i] 为 True 并 break
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        # dp[i] 表示 s[: i] 能否被 wordDict 表示
        dp = [False for _ in range(n + 1)]
        # 空字符串可以被表示
        dp[0] = True

        for i in range(1, n + 1):
            # 当判断 s[: i] 能否被 wordDict 表示时, 需要使用 j 将 s[: i] 切分为 s[: j] 和 s[j: i], 然后判断 dp[j] and s[j: i] in wordDict:
            # dp[j]: 表示 s[: j] 能否被表示
            # s[j: i] in wordDict: 表示s[j: i] 能否被表示
            # 遍历过程中, 一旦二者同时成立, 则说明 s[: i] 可以被 wordDict 表示, 直接更新 dp[i] 为 True 并 break
            for j in range(0, i):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]