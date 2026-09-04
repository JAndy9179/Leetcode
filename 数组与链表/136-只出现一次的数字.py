from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict = defaultdict(int)
        for n in nums:
            num_dict[n] += 1

        for k, v in num_dict.items():
            if v == 1:
                return k