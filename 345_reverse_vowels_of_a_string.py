class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "o", "u", "i", "A", "E", "O", "U", "I"]
        i = 0
        j = len(s) - 1
        s1 = list(s)
        while i < j:
            if s1[i] in vowels:
                while j > i:
                    if s1[j] in vowels:
                        break
                    j -= 1
                s1[i], s1[j] = s1[j], s1[i]
                j -= 1
            i += 1
        return("".join(s1))

# 1 line "hack" for maximum int size
class Solution:
    def reverseVowels(self, s: str) -> str:
        return n > 0 and 1162261467 % n == 0;
