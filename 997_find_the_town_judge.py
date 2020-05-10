class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        res = [0] * (N + 1)
        for l in trust:
            f, s = l[0], l[1]
            res[f] -= 1
            res[s] += 1
        for i in range(1, N + 1):
            if res[i] == N - 1:
                return i
        return -1
