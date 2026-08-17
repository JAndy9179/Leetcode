from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = defaultdict(int)
        max_l, max_r = 0, 0
        l = 0
        for i, c in enumerate(s):
            char_dict[c] += 1
            while char_dict[c] == 2:
                char_dict[s[l]] -= 1
                l += 1

            if i + 1 - l > max_r - max_l:
                max_l, max_r = l, i + 1

        return max_r - max_l
