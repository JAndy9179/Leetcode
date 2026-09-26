"""
思路: 贪心算法

实时维护最远可以到达的位置 max_step: 依次遍历除了最后一个位置外的每一个位置, 然后看看从当前位置最远可以跳多远, 如果能跳的比之前的最远位置还远, 则更新当前所能到达的最远位置为 max(max_step, i + nums[i])


注意: 

对于 [0, 2, 3] 这样的例子, 由于第 0 个位置最远只能跳到 0, 无法再继续向后跳, 因此需要设置判断条件: 当 max_step < i + 1 时直接 return False
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_step = 0
        target = len(nums) - 1

        for i in range(len(nums) - 1):
            max_step = max(max_step, i + nums[i])
            if i < len(nums) - 1 and max_step < i + 1:
                return False

        return max_step >= target