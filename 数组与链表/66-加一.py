from typing import List


""" python 数组与链表/66-加一.py """


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = 0
        for i in range(
            len(digits) - 1,    # start
            -1,                 # stop: 最后要遍历到 i = 0, 因此 stop 需要再往前设置一位为 -1, 和正向同理
            -1                  # step: 每次循环后索引 -1
        ):
            if i == len(digits) - 1:
                temp = digits[i] + 1
                digits[i] = temp % 10
                s = temp // 10
            else:
                if s > 0:
                    temp = digits[i] + s
                    digits[i] = temp % 10
                    s = temp // 10
            
        if s > 0:
            return [1] + digits
        else:
            return digits


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne(digits=[9, 9]))
