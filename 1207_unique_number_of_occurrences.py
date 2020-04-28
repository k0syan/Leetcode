class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for a in arr:
            if a in d:
                d[a] += 1
            else:
                d[a] = 1
        val = list(d.values())
        if len(val) != len(set(val)):
            return False
        return True
