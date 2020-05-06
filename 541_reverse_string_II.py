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

# Beautiful but slow
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        ans = ""
        a = list(s)
        for i in range(0, len(a), 2 * k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)
