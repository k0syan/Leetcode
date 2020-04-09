class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = ""
        i = len(num1) - 1
        if len(num1) > len(num2):
            i = len(num2) - 1
        c = 0
        n, m = len(num1) - 1, len(num2) - 1
        while i >= 0:
            d1 = int(num1[n])
            d2 = int(num2[m])
            dn = d1 + d2 + c
            if dn > 9:
                c = 1
                dn = dn % 10
            else:
                c = 0
            ans = str(dn) + ans
            i -=1
            m -= 1
            n -= 1
        while m >=0:
            if c == 1 and num2[m] == "9":
                ans = "0" + ans
            else:
                ans = str(int(c) + int(num2[m])) + ans
                c = 0
            m -= 1
        while n >=0:
            if c == 1 and num1[n] == "9":
                ans = "0" + ans
            else:
                ans = str(int(c) + int(num1[n])) + ans
                c = 0
            n -= 1
        if c == 1:
            ans = "1" + ans
        return ans
