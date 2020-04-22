# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        s, e = 0, m - 1
        i = m
        while s < n and e >= 0:
            v = binaryMatrix.get(s, e)
            if v == 0:
                s += 1
            else:
                i = min(i, e)
                e -= 1
        if i < m:
            return i
        return -1
