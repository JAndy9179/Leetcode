"""
思路: 动态规划

dp[i][j]: 表示 s[i: j + 1] 是不是回文子串

有个细节需要注意, 这里面的 l 要从右往左遍历. 如果 l, r 都是从左往右, 就会出现 dp[l][r] = dp[l + 1][r - 1] 时, dp[l + 1][r - 1] 还是默认值的情况
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j]: 表示 s[i: j + 1] 是不是回文子串
        n = len(s)
        max_len = 0
        max_l, max_r = 0, 0
        dp = [[False] * n for _ in range(n)]

        # 1. 初始化 dp 数组
        for i in range(n):
            dp[i][i] = True

        # 2. 更新 dp 数组
        for l in range(n - 2, -1, -1):
            for r in range(l + 1, n):
                # case 1: 如果字符串的左右端点都不一样, 那就肯定不是回文子串
                if s[l] != s[r]:
                    dp[l][r] = False
                else:
                    # case 2.1: x, xx, xyx 这几种情况都是 True
                    if r - l < 3:
                        dp[l][r] = True
                    else:
                        dp[l][r] = dp[l + 1][r - 1]

                if dp[l][r] == True and (r - l + 1) > max_len:
                    max_len = r - l + 1
                    max_l, max_r = l, r

        return s[max_l: max_r + 1]