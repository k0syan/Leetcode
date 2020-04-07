class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        retList = list(range(1, len(nums) + 1))
        return list(set(retList) - set(nums))
