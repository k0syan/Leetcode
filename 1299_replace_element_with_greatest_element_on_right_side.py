class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mi = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], mi = mi, max(mi, arr[i])
        return arr
