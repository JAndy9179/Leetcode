from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        used = [[0] * n for _ in range(m)]
        ans = 0

        def isValid(i, j):
            if 0 <= i < m and 0 <= j < n and used[i][j] == 0 and grid[i][j] == "1":
                return True
            return False

        def search(i, j):
            if not isValid(i, j):
                return

            used[i][j] = 1
            search(i, j + 1)
            search(i, j - 1)
            search(i + 1, j)
            search(i - 1, j)

        for i in range(m):
            for j in range(n):
                if used[i][j] == 0 and grid[i][j] == "1":
                    search(i, j)
                    ans += 1

        return ans
