class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1:
            return stones[0]
        ss = stones
        while n != 1:
            n = len(ss)
            if n == 0:
                return 0
            if n == 1:
                return ss[0]
            ss.sort()
            l = ss[n - 1]
            p = ss[n - 2]
            if l - p == 0:
                ss = ss[:-2]
            else:
                ss = ss[:-2]
                ss.append(l - p)
