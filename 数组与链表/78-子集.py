"""
思路:

看起来很简单但是实现比较难, 这里使用了别人的方法: 遍历 len(nums) 次, 每次都在 res 中已有的结果中追加一个 nums[i] 作为新的结果并 append 到 res 中

例如 nums = [1, 2, 3], 设 res = [[]]: 
    第一轮遍历后 res 的结果为: [[], [1]]
    第二轮遍历后 res 的结果为: [[], [1], [2], [1, 2]]
    第三轮遍历后 res 的结果为: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]

        for n in nums:
            # print(f"[n={n}, len(res) = {len(res)}]")
            for j in range(len(res)):
                res.append(res[j] + [n])

        return res