class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k != 0:
            tmp = nums[len(nums) - 1]
            del nums[-1]
            nums.insert(0, tmp)
            k -= 1
                
