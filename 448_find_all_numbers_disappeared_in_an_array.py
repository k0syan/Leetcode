class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        retList = list(range(1, len(nums) + 1))
        return list(set(retList) - set(nums))
    
# Without extra space
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            tmp = abs(nums[i]) - 1
            if nums[tmp] > 0:
                nums[tmp] *= -1
        retList = []
        for i in range(len(nums)):
            if nums[i] > 0:
                retList.append(i + 1)
        return retList
