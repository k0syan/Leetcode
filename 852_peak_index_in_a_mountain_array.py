class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                return i
            
# Binary search
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        s, e = 0, len(A) - 1
        while s < e:
            mid = (s + e) // 2
            if A[mid] < A[mid + 1]:
                s = mid + 1
            else:
                e = mid
        return s
    
# One liner
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))
