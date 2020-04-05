class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        n = num
        if n == 1:
            return True
        if n <= 3:
            return False
        f = sqrt(n) - round(sqrt(n)) == 0
        return (n & (n - 1) == 0 and f)
