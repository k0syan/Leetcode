class Solution:
    def arrangeCoins(self, n: int) -> int:
        t = 0
        k = 0
        if n == 0:
            return 0
        for i in range(1, n + 1):
            t += i
            if t == n:
                return i
            elif t > n:
                return i - 1
            
