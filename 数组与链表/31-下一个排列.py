"""
思路: 

可以先看几个例子:
1.      1 2 [5 4 3      -->         1 3 2 4 5
2.      1 4 2 3 [5      -->         1 4 2 5 3

以第一个例子为例, 只需要按照以下步骤就可以得到下一个排列:
1. 从后往前找到不再降序后的第一个位置(记为 l), 然后再降序序列中找到刚好大于 nums[l] 的位置(记为 r)   --   1 (2) 5 4 (3)
2. 交换 nums[l] 和 nums[r]                                                                     --   1 (3) 5 4 (2)
3. 之后保持 nums[l + 1: ] 后面升序就行了                                                        --   1 3 2 4 5

Q: 这里有个关键问题, 为什么要从后往前找到不再降序后的第一个位置?
A: 还是以第一个例子来说, 很显然如果要得到它的下一个排列, 如果从降序部分(5, 4, 3)操作的话, 只能得到比原来小的排列, 所以只能继续向前找到不再降序后的第一个位置
"""


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 这里位置 l 右边的序列应该保持降序排列
        # 在这部分降序排列的序列中, 找到刚好大于 nums[l] 的最小的数 nums[r]
        l, r = 0, 0
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if i != n - 1 and nums[i] < nums[i + 1]:
                l = i
                break
        for i in range(n - 1, l, -1):
            if nums[i] > nums[l]:
                r = i
                break

        if l == 0 and r == 0:
            # 特殊情况: 就是整个数组全是降序排列, 此时没有下一个排列, 直接 nums.reverse() 并返回
            nums.reverse()
            return
        
        nums[l], nums[r] = nums[r], nums[l]
        for i in range(l + 1, n - 1):
            for j in range(l + 1, n - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
