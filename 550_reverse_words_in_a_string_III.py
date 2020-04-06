class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        for i in range(len(l)):
            w = l[i]
            l[i] = w[::-1]
        return " ".join(l)
            
