class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        sa = ""
        for s in S:
            if s == "#":
                if len(sa) > 0:
                    sa = sa[:-1]
            else:
                sa += s
        ta = ""
        for t in T:
            if t == "#":
                if len(ta) > 0:
                    ta = ta[:-1]
            else:
                ta += t
        return sa == ta
