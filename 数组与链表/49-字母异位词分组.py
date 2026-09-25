"""
思路:

可以用 Counter 统计每个字符串的字符个数, 然后用字典进行分组. 只不过 Counter 是不可哈希的, 所以需要在外面套一层 tuple.

当然, 这里直接使用 tuple(sorted(s)) 也能有同样的效果.
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import defaultdict

        sd = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            sd[key].append(s)

        res = []
        for k, v in sd.items():
            res.append(v)

        return res