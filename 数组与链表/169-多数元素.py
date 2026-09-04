from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1
            if num_dict[num] > (n // 2):
                return num
