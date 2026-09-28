"""
思路一:

题目说按照红色、白色、蓝色顺序(也就是 0, 1, 2)排列, 其实就是升序排列, 随便选个排序算法就 OK 了, 而且题目其实也有提示(必须在不使用库内置的 sort 函数的情况下解决这个问题)


思路二: 双指针

使用 p0 表示下一个 0 应该放的位置, p2 表示下一个 2 应该放的位置, i 表示当前正在检查的位置:
    当 nums[i] == 0 时, 与 p0 交换, 且 p0 和 i 都右移
    当 nums[i] == 2 时, 与 p2 交换, p2 左移但 i 不动, 因为换过来的数不一定是 0, 所以还需要下一轮循环去判断
这样的话 0 元素都往左边移, 2 都往右边移, 1 留在中间位置即可
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        for i in range(n - 1):
            for j in range(n - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

    def sortColors_2(self, nums: list[int]) -> None:
        i = 0
        p0, p2 = 0, len(nums) - 1

        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            else:
                i += 1