class Solution:
    def isHappy(self, n: int) -> bool:
        memo = set()
        while n != 1 and n not in memo:
            memo.add(n)
            ne = 0
            while n > 0:
                a = n % 10
                n = n // 10
                ne += a * a
            n = ne
        return n == 1
        
