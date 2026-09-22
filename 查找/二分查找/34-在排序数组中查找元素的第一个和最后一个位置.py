"""
思路:

首先题目要求时间复杂度 O(log n), 想到用二分查找; 然后要求得到两个位置, 所以就想到分别用两次二分查找, 一次得到左边界一次得到右边界
    对于得到左边界得二分查找, 要求当 nums[mid] >= target 的时候就要 r = mid - 1, 这样退出循环的时候, l 对应的位置就是左边界
    对于得到右边界得二分查找, 要求当 nums[mid] <= target 的时候就要 l = mid + 1, 这样退出循环的时候, r 对应的位置就是右边界

注:
其实主要就是想到用两次二分查找, 以及两个二分查找内的判断条件(即 nums[mid] >= target 和 nums[mid] <= target), 至于剩下的到底是返回 l 还是 r, 以及分别什么时候返回 -1 这种问题, 多提交几次试几次就知道了
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def binary_search_left(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1

            # 最终 l 对应的位置是左边界
            if 0 <= l < len(nums) and nums[l] == target:
                return l
            return -1

        def binary_search_right(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1

            # 最终 r 对应的位置是右边界
            if 0 <= r < len(nums) and nums[r] == target:
                return r
            return -1

        l = binary_search_left(nums, target)
        r = binary_search_right(nums, target)
        return [l, r]