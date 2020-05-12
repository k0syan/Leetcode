class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        m = max(candies)
        for c in candies:
            if c + extraCandies >= m:
                res.append(True)
            else:
                res.append(False)
        return res
