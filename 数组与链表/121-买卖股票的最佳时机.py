class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        max_profit = 0
        for p in prices:
            if not stack or stack[-1] > p:
                stack.append(p)
            else:
                max_profit = max(max_profit, p - stack[-1])
        
        return max_profit