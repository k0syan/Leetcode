class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        mi = prices[0]
        prof = 0
        for p in prices:
            mi = min(mi, p)
            prof = max(prof, p - mi)
        return prof
