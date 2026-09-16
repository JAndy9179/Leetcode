"""
思路:

只有满足条件 right > 0 and left < right, 才能保证左括号被右括号抵消掉
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def generate(left, right, temp):
            if left == 0 and right == 0:
                res.append(''.join(temp))
                return

            if left > 0:
                temp.append('(')
                generate(left - 1, right, temp)
                temp.pop()
            if right > 0 and left < right:
                temp.append(')')
                generate(left, right - 1, temp)
                temp.pop()

        generate(n, n, [])
        return res