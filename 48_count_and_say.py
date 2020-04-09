def nextIn(cur) -> str:
        if cur == "1":
            return "11"
        res = ""
        i = 1
        cnt = 1
        while i < len(cur):
            if cur[i] == cur[i - 1]:
                cnt += 1
            else:
                res += str(cnt) + cur[i - 1]
                cnt = 1
            if i == len(cur) - 1:
                    res += str(cnt) + cur[i]
            i += 1
        return res

class Solution:    
    def countAndSay(self, n: int) -> str:
        ans = "1"
        if n == 1:
            return ans
        else:
            for i in range(1, n):
                ans = nextIn(ans)
        return ans
