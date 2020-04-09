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
            
