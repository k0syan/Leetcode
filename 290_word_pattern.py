class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        p = list(pattern)
        s = str.split()
        if len(p) != len(s):
            return(False)
        x = list(set(zip(p, s)))
        return(len(x) == len(set(p)) == len(set(s)))
