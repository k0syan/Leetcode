class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-", "").upper()
        ans = ""
        while len(S):
            if len(S) >= K:
                if len(ans) > 0:
                    ans = S[-K:] + "-" + ans
                else:
                    ans = S[-K:]
                S = S[:-K]
            else:
                if len(ans) > 0:
                    ans = S + "-" + ans
                else:
                    ans = S
                break
        return(ans)
    
# Pythonic quick solution

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-", "").upper()[::-1]
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]
