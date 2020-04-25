class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lp = len(nums) - 1
        for i in range(lp, -1, -1):
            if (i + nums[i] >= lp):
                lp = i
        return lp == 0
