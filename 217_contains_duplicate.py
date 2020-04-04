class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nd = {}
        for n in nums:
            if n in nd:
                return(True)
            else:
                nd[n] = 1
        return(False)
