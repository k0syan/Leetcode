class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            c = s[i]
            if c in d:
                d[c] = (d[c][0] + 1, i)
            else:
                d[c] = (1, i)
        for x in d.values():
            if x[0] == 1:
                return x[1]
        return -1
    
# Faster solution
class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1


