class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]
    
# XoR 
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for c in s + t:
            ans ^= ord(c)
        return chr(ans)
