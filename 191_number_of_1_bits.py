class Solution:
    def hammingWeight(self, n: int) -> int:
        x = list(str(bin(n)))
        c = 0
        for a in x:
            if a == "1":
                c += 1
        return c
    
# With bit operations

class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
    
        while n:
            n = n & (n - 1)
            c += 1
        return c
        
