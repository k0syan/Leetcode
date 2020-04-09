class Solution:
    def findComplement(self, num: int) -> int:
        b = "{0:b}".format(num)
        nb = ""
        for c in b:
            nb += "1"
        return int(nb, 2) ^ num
