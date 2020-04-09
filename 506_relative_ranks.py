class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        sn = nums.copy()
        sn.sort()
        n = len(nums)
        for i in range(n):
            ins = sn.index(nums[i])
            if ins == n - 1:
                nums[i] = "Gold Medal"
            elif ins == n - 2:
                nums[i] = "Silver Medal"
            elif ins == n - 3:
                nums[i] = "Bronze Medal"
            else:
                nums[i] = str(n - ins)
        return nums
