class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        lp = 0
        used = False
        for c in d:
            if d[c] % 2 == 1:
                if used:
                    lp += d[c] - d[c] % 2
                    continue
                used = True
                lp += d[c]
            else:
                lp += d[c]
        return lp
