# Intuitive
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(x * x for x in A)
    
# Better
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        s, e = 0, len(A) - 1
        while s <= e:
            start, end = abs(A[s]), abs(A[e])
            if start > end:
                res[e - s] = start * start
                s += 1
            else:
                res[e - s] = end * end
                e -= 1
        return res
