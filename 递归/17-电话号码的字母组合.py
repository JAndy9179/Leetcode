class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        num_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []

        def search(depth, temp):
            if depth == len(digits):
                res.append(''.join(temp))
                return

            d = digits[depth]
            chars = num_dict[d]
            for c in chars:
                temp.append(c)
                search(depth + 1, temp)
                temp.pop(-1)

        search(0, [])
        return res