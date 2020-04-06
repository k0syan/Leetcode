class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        tot = 1
        i = 2
        x = int(num ** 0.5) + 1
        while i < x:
            if num % i == 0:
                tot += i + num // i
            i += 1
        return tot == num
        
