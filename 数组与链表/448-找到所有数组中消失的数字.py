from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = set(n for n in nums)
        res = []
        for i in range(1, len(nums) + 1):
            if i not in seen:
                res.append(i)

        return res
            