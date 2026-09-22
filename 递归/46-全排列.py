"""
思路:

唯一需要注意的就是进入下一层的时候, 把当前选择的加入 selected, 然后需要在 candidates 中去掉该数字, 这样下一层的时候就只会在剩下的数字中去选
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def dfs(candidates, selected):
            if not candidates:
                res.append(selected.copy())
                return

            for c in candidates:
                temp = candidates.copy()
                temp.remove(c)
                selected.append(c)
                dfs(temp, selected)
                selected.pop(-1)

        dfs(nums, [])
        return res


print(Solution().permute([1, 2, 3]))