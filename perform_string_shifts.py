class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        ts = 0
        for sh in shift:
            d, c = sh[0], sh[1]
            if d == 0:
                ts += c
            else:
                ts -= c
        n = len(s)
        if ts > n or abs(ts) > n:
            ts = ts % n
        if ts < 0:
            ts = n + ts
            s = s[ts:] + s[:ts]
        else:
            s = s[ts:] + s[:ts]
        return s
