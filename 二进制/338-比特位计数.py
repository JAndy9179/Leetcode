from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        i = 0
        while i <= n:
            cnt = 0
            t = i
            while t > 0:
                cnt += t & 1
                t = t >> 1
            
            res.append(cnt)
            i += 1

        return res