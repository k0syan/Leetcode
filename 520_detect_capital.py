class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        l = word.lower()
        if l == word:
            return True
        f = False
        if word[0].lower() != word[0]:
            f = True
        al = True
        au = True
        for i in range(1, len(word)):
            x = word[i]
            if x.lower() != x:
                al = False
            else:
                au = False
        return (f and au) or al
