"""
思路:

首先需要将 intervals 按照 intervals[i][0] 升序排序, 这样才能依次遍历 intervals 判断要不要将当前区间合并. 将第一个元素 intervals[0] 添加到栈中, 之后执行如下操作, 对于 intervals 中的剩余元素:
1. 如果 intervals[i][0] > res[-1][1] (如 res 的最后一个元素是 [1, 3], interval[i] 是 [4, 7]), 此时显然合并不了, 因此直接 res.append(intervals[i])
2. 其余情况只需比较 res 中的栈顶元素 tap_vals 与 intervals[i], 左边界取二者第一个元素的最小值, 右边界取二者第二个元素的最大值, 然后拼接成新的合并区间, 并 append 到栈顶
"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda intervals: intervals[0])
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                top_vals = res.pop(-1)
                l = min(top_vals[0], intervals[i][0])
                r = max(top_vals[1], intervals[i][1])
                res.append([l, r])
        
        return res