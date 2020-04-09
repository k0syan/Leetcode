class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s = nums.copy()
        s.sort()
        fi = 0
        li = 0
        for i in range(len(nums)):
            if s[i] != nums[i]:
                fi = i
                break
        for i in range(len(nums) - 1, 0, -1):
            if s[i] != nums[i]:
                li = i
                break
        if li > fi:
            return li - fi + 1
        return li - fi
