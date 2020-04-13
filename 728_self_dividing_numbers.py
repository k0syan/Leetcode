class Solution:
    def check(n: int):
        a = n
        while n != 0:
            print(n)
            x = n % 10
            print(x)
            if x == 0:
                return False
            if a % x != 0:
                return False
            n = n // 10
        return True
        
        
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right + 1):
            if Solution.check(i):
                ans.append(i)
        return ans
