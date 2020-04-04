class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lc = {}
        tc = {}

        for s1 in s:
            if s1 in lc:
                lc[s1] += 1
            else:
                lc[s1] = 1

        for t1 in t:
            if t1 in tc:
                tc[t1] += 1
            else:
                tc[t1] = 1

        return(lc == tc)
    
# One liner

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
