class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        res = []
        for d in num:
            while k and res and res[-1] > d:
                res.pop()
                k -= 1
            res.append(d)
        while k != 0:
            res = res[:-1]
            k -= 1
        while res and res[0] == "0":
            res = res[1:]
        if not res:
            return "0"
        return "".join(res)
