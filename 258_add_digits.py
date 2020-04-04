class Solution:
    def addDigits(self, num: int) -> int:
        n = num
        while True:
            a = 0
            while n != 0:
                a += n % 10
                n = n // 10
            n = a
            if n // 10 == 0:
                break
        return(n)
