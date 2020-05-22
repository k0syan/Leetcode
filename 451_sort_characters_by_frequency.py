class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
        ans = ""
        i = len(d) - 1
        while i >= 0:
            key = list(d.keys())[i]
            ans += key * d[key]
            i -= 1
        return ans
