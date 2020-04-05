class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True
        if num <= 3:
            return False
        f = sqrt(num) - round(sqrt(num)) == 0
        return (num & (num - 1) == 0 and f)

# Better solution

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        return (num & (num - 1) == 0 and (num - 1) % 3 == 0)
    
# With bits

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return (num > 0) and ((num & (num - 1)) == 0) and ((num & 0x55555555) == num);
