class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        if len(nums) % 2 == 0:
            idx_l, idx_r = len(nums) // 2 - 1, len(nums) // 2
            return (nums[idx_l] + nums[idx_r]) / 2
        else:
            idx = len(nums) // 2
            return nums[idx]