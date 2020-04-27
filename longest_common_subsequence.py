class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        d = [[0] * (m + 1)] * (n + 1)
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    d[i+1][j+1] = d[i][j] + 1
                else:
                    d[i+1][j+1] = max(d[i][j+1], d[i+1][j])
        return d[n][m]
