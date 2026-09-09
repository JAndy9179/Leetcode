"""
思路: 左右指针

左指针 left: 表示 nums[: left] 已经符合题目要求
右指针 right: 从零开始遍历 nums 的索引
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        n = len(nums)
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
