# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        mi = 1
        ma = n
        a = (mi + ma) // 2
        g = guess(a)
        while g != 0:
            if g == -1:
                ma = a
            else:
                mi = a + 1
            a = (mi + ma) // 2
            g = guess(a)
        return(a)
