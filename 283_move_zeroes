class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tn = 0
        i = 0
        while i < len(nums):
            c = nums[i]
            if c == 0:
                tn += 1
                del nums[i]
                i -=1
            i += 1
        for i in range(tn):
            nums.append(0)
        print(nums)
