"""
思路: 动态规划

以第 i 家作为最后一次偷窃时, 能获得的最大金额记为 dp[i]

状态转移方程: dp[i] = nums[i] + max(dp[:i - 1])
(因为必须偷第 i 家，根据规则相邻两家不能同时偷，所以第 i-1 家一定不能偷，只能从 dp[0] 到 dp[i-2] 中挑一个最大的，再加上 nums[i]。)

返回结果: max(dp)
(最优解不一定偷最后一家, 而是比较所有情况的最大值)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        dp = [0 for _ in range(len(nums))]
        dp[0], dp[1] = nums[0], nums[1]

        for i in range(2, len(nums)):
            dp[i] = nums[i] + max(dp[: i - 1])

        return max(dp)