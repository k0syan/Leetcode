class Solution:
    def checkRecord(self, s: str) -> bool:
        d = {}
        l = 0
        for i in range(len(s)):
            c = s[i]
            if c == "A":
                l = 0
                if c in d:
                    return False
                d[c] = 1
            if c == "L":
                l += 1
                if l > 2:
                    return False
            else:
                l = 0
        return True
