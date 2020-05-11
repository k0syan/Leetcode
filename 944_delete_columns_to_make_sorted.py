class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        ans = 0
        for c in zip(*A):
            if any(c[i] > c[i+1] for i in range(len(c) - 1)):
                ans += 1
        return ans
