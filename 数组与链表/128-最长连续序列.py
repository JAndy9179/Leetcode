"""
思路 1:

先 set() 去重再 sort() 排序, 最后对排好序的数组计算连续序列的最长长度


思路 2:

还是先去重, 然后遍历数组中的每个元素, 尝试以当前元素 x 为起点, 不断匹配 x+1, x+2, ... 是否在数组中, 得到当前节点为起始节点的最长序列, 并不断更新最终答案
这里还有一个小优化, 就是对于元素 n, 如果 n - 1 也在数组中就直接跳过, 因为以 n 为起始节点的最大长度肯定会小于以 n - 1 为起始节点的最大长度
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        
        l = 0
        max_len = 0
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                continue
            else:
                max_len = max(max_len, i - l + 1)
                l = i + 1
        
        return max(max_len, len(nums) - l)

    def longestConsecutive_2(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for n in num_set:
            if n - 1 not in num_set:
                curr_len = 1
                curr_num = n

                while curr_num + 1 in num_set:
                    curr_len += 1
                    curr_num = curr_num + 1

                max_len = max(max_len, curr_len)

        return max_len
