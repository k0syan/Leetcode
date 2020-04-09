class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        candies.sort()
        n = len(candies)
        cnt = 1
        i = 1
        while i < n and cnt < n / 2:
            if candies[i] > candies[i - 1]:
                cnt += 1
            i += 1
        return cnt
    
# set solution

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        d = set()
        for c in candies:
            d.add(c)
        return min(len(candies) // 2, len(d))
            
