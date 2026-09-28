"""
思路: 

和岛屿问题差不多, 就是遍历各个位置作为起始位置, 然后每个位置依次往四个方向尝试探索, 能找到目标字符就返回 True, 不能就返回 False

注意:
1. 这里一定要用 temp.pop() 不能用 temp.remove(), 要不然出现重复元素的时候它会 remove 掉从左到右出现的第一个相同元素, 破坏当前路径的真实顺序
2. 这里使用了 found 来接收四个方向返回的状态而不是直接 return, 这样 found 为 False 的时候方便回溯 used 和 temp
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def isValid(i, j):
            if 0 <= i < m and 0 <= j < n and used[i][j] != 1:
                return True
            return False

        def move(i, j, temp):
            if not isValid(i, j):
                return False

            temp.append(board[i][j])
            if ''.join(temp) != word[:len(temp)]:
                # 当前缀就不匹配的时候, 直接返回 False, 就不用继续往下走了
                temp.pop()
                return False

            used[i][j] = 1
            if len(temp) == len(word) and ''.join(temp) == word:
                # 已经找到目标字符串, 返回 True
                return True

            # 前缀匹配且 len(temp) 还不等于 len(word) 的时候, 继续朝四个方向探索
            found = (
                move(i, j + 1, temp)
                or move(i + 1, j, temp)
                or move(i, j - 1, temp)
                or move(i - 1, j, temp)
            )
            if not found:
                used[i][j] = 0
                temp.pop()
            return found

        for i in range(m):
            for j in range(n):
                used = [[0] * n for _ in range(m)]
                if move(i, j, []):
                    return True

        return False