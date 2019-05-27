class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewelry = list(J)
        mine = list(S)
        total = 0
        for m in mine:
            if m in jewelry:
                total += 1
        return total