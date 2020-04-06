class Solution:
    def fib(self, N: int) -> int:
        if N == 0: return 0
        if N == 1: return 1
        return self.fib(N-1) + self.fib(N-2)
    
# Binet's formula
class Solution:
    def fib(self, N: int) -> int:
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** N + 1) / 5 ** 0.5)
    
###
https://www.sciencedirect.com/science/article/pii/S0195669807000595
