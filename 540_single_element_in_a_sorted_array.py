class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        c = nums[0]
        i = 1
        while i < len(nums):
            if c == nums[i]:
                i += 1
                c = nums[i]
                i += 1
            else:
                return c
        return c
