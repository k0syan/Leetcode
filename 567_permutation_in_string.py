# Intuitive
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1s = list(s1)
        s1s.sort()
        n = len(s1)
        for i, c in enumerate(s2):
            if c in s1:
                tmp = list(s2[i:i+n])
                tmp.sort()
                if tmp == s1s:
                    return True
        return False
