from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = defaultdict(int)
        for i, n in enumerate(nums):
            if target - n in num_dict.keys():
                return [i, num_dict[target - n]]
            else:
                num_dict[n] = i

        return []