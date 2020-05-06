class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        ans = ""
        while i < len(s):
            tmp = s[i :i + k]
            tmp = tmp[::-1]
            ans += tmp
            ans += s[i+k:i+2*k]
            i += k
            i += k
        return ans
