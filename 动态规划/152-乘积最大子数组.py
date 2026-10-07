"""
思路: 动态规划

本题和 "最大子数组和" 的本质区别是:
- 加法: 加上一个, 和只会单调地变大或变, 所以只需维护"以当前位置结尾的最大和"
- 乘法: 乘以一个负数会让符号翻, 即之前"最小"的乘积, 乘上负数后反而会变成最大的正数

因此本题需要维护 maxs 和 mins 两个数组, 同时记录以 nums[i] 结尾的最大乘积和最小乘积, 更新的时候需要比较三个值: mins[i-1] * nums[i], maxs[i-1] * nums[i], nums[i]
- mins[i] = min(mins[i-1] * nums[i], maxs[i-1] * nums[i], nums[i]): 
    取 nums[i]: 前面的乘积拖累太大，重新开始
    取 maxs[i-1] * nums[i]: nums[i] 为正时，延续最大值
    取 mins[i-1] * nums[i]: nums[i] 为负时，负负得正，最小值反而产生最大值
- maxs[i] = max(mins[i-1] * nums[i], maxs[i-1] * nums[i], nums[i]): 同理

最后再比较 max(mins[i], maxs[i]) 得到 dp[i] (以 nums[i] 结尾的最大乘积)
"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        mins = [nums[0] for _ in range(n)]
        maxs = [nums[0] for _ in range(n)]
        dp = [nums[0] for _ in range(n)]

        for i in range(1, n):
            mins[i] = min(mins[i - 1] * nums[i], maxs[i - 1] * nums[i], nums[i])
            maxs[i] = max(mins[i - 1] * nums[i], maxs[i - 1] * nums[i], nums[i])
            dp[i] = max(mins[i], maxs[i])

        return max(dp)