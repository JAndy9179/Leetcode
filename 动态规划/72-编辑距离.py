"""
思路:

举个例子, 将 horse 转化成 ros, 可以通过以下几种方式:
1. 若我们已经知道了从 horse 转化成 ro 的编辑距离为 a, 则从 horse 转化为 ros 的距离可以为 a + 1 (horse 先用 a 步转化成 ro, 再在 ro 末尾添加个字母)
2. 若我们已经知道了从 ros 转化成 hors 的编辑距离为 b, 则从 ros 转化为 horse 的距离可以是 b + 1 (ros 先用 b 步转化成 hors, 再在 hors 末尾添加个字母)
3. 若我们已经知道了从 hors 转化成 ro 的编辑距离为 c, 则从 horse 转化为 ros 的距离可以是 c + 1 (horse 先用 c 步将前缀 hors 转化成 ro, 此时字符串变为 ro, 再将末尾的 e 替换为 s)

因此可以设置 dp 数组, 其中 dp[i][j] 表示 word1 的前 i 个字符转化为 word2 的前 j 个字符的编辑距离, 然后通过下面的方式更新:
1. 当末尾字符需要替换的时候: dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
2. 当末尾字符不需要替换的时候: dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 1. 初始化
        for i in range(1, n + 1):
            dp[0][i] = dp[0][i - 1] + 1
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + 1

        # 2. 更新
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

        return dp[m][n]
