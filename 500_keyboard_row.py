class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        retList = []
        for w in words:
            word = set(w.lower())
            if word <= first or word <= second or word <= third:
                retList.append(w)
        return retList
