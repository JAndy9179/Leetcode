"""
思路:

可以先观察一下, 对于数列 [0, 1, 2, 4, 5, 6, 7] 来说, 一共有以下几种旋转方式: 
    从 0 向左旋转: [0, 1, 2, 4, 5, 6, 7]
    从 1 向左旋转: [1, 2, 4, 5, 6, 7, 0]
    从 2 向左旋转: [2, 4, 5, 6, 7, 0, 1]
    从 4 向左旋转: [4, 5, 6, 7, 0, 1, 2]
    从 5 向左旋转: [5, 6, 7, 0, 1, 2, 4]
    从 6 向左旋转: [6, 7, 0, 1, 2, 4, 5]
    从 7 向左旋转: [7, 0, 1, 2, 4, 5, 6]

首先题目要求时间复杂度 O(log n), 想到用二分查找; 其次通过观察可以发现, 不管怎么旋转, 下标 mid 的左右两侧必有一侧是有序的(循环之后取 mid 也是同理), 共有以下三种情况: 
    从 0 旋转的时候: nums[l] <= nums[mid] <= nums[r]          <-->    两边都有序
    从 1 ~ 4 旋转的时候: nums[l] <= nums[mid] >= nums[r]      <-->    nums[l: mid + 1] 这部分有序
    从 5 ~ 7 旋转的时候: nums[l] >= nums[mid] <= nums[r]      <-->    nums[mid: r + 1] 这部分有序
    (这里加等号是为了处理 mid 等于 l 或 r 的情况)

因此我们可以通过判断 nums[mid] 和 nums[l], nums[r] 的大小关系, 来判断当前区间的哪半部分是有序的, 然后看看 target 是不是在这个有序的区间中, 如果不是的话就在另外的半区去找
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid] >= nums[r]:
                # 此时左半边有序, 先在左边寻找, 找不到再找另一边
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] >= nums[mid] <= nums[r]:
                # 此时右半边有序, 先在右边寻找, 找不到再找另一边
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # 此时是正常的二分排序
                if target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1

