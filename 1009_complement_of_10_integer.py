class Solution:
    def bitwiseComplement(self, N: int) -> int:
        b = "{0:b}".format(N)
        nb = ""
        for c in b:
            nb += "1"
        return int(nb, 2) ^ N
