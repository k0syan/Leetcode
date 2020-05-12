class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d = {}
        for n in A:
            if n in d:
                return n
            d[n] = 1
