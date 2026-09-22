"""
思路: 递归

细节 1: 需要 append selected.copy() 而不是 selected. 
    因为如果不 copy, 那么 append 进 res 的其实都是同一个地址, 而这个地址上的对象会在递归完成后变为空列表, 因此最后 res 中全是空列表
    相当于 selected 是一张可以反复擦写的草稿纸, 递归过程中一直在使用同一张草稿纸, 每次得到结果后需要先将草稿纸拍个照(.copy())后然后把照片收集起来, 之后再擦去草稿纸上的内容接着递归(.pop(-1))

细节 2: 每一轮递归的时候, candidates 参数只需要传入 candidates[i: ]
    假如 candidates = [2, 3, 6, 7], target = 7, 第一层递归如果遍历完了 c = 2 之后, 所有包含 2 的情况已经被全部取到了, 后续该轮到 c = 3 的时候再从 2 开始取就会有重复


当然还有一种更简单的方式, 就是不进行 candidates[i: ] 处理, 直接传入 candidates, 只不过在 append 的时候先判断是不是当前组合已经被添加到 res 中了, 判断方法可以维护一个 seen, 并使用 Counter 统计当前 selected 列表各个数字的个数, 来判断这个组合是否已经被添加, 这种我也试过不会超时
"""


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(candidates, selected, target):
            if target < 0:
                return
            if target == 0:
                res.append(selected.copy())
                return

            for i, c in enumerate(candidates):
                selected.append(c)
                dfs(candidates[i: ], selected, target - c)
                selected.pop(-1)

        dfs(candidates, [], target)
        return res

    def combinationSum_2(self, candidates: list[int], target: int) -> list[list[int]]:
        from collections import Counter


        res = []
        seen = []

        def dfs(candidates, selected, target):
            if target < 0:
                return
            if target == 0:
                counter = Counter(selected)
                if counter not in seen:
                    res.append(selected.copy())
                    seen.append(counter)
                return

            for c in candidates:
                selected.append(c)
                dfs(candidates, selected, target - c)
                selected.pop(-1)

        dfs(candidates, [], target)
        return res