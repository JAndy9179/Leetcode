class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        max_len = 0
        for c in s:
            while c in stack:
                stack.pop(0)

            stack.append(c)
            max_len = max(max_len, len(stack))

        return max_len
