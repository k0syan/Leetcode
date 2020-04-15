class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [1] * length
        for i in range(1, length):
            ans[i] = ans[i - 1] * nums[i - 1]
        r = 1
        print(ans)
        for i in range(length - 1, -1, -1):
            ans[i] *= r
            r *= nums[i]
        return ans
        
