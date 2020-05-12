# Greedy
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return ([x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1])

# Effective one
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]
            
            if A[i] % 2 == 0:
                i += 1
            if A[j] % 2 == 1:
                j -= 1
        return A
