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
