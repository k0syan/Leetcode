class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i = 1
        while i < len(prices):
            m = prices[i] - prices[i - 1]
            if m > 0:
                res += m
            i += 1
        return res
