class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True
        for i in range(num // 2 + 1):
            if i * i == num:
                return True
            if i * i > num:
                return False
        return False
