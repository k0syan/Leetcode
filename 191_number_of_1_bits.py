class Solution:
    def hammingWeight(self, n: int) -> int:
        x = list(str(bin(n)))
        c = 0
        for a in x:
            if a == "1":
                c += 1
        return c
        
