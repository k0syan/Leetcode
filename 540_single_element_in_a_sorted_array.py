# Greedy
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

# XoR
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans ^= n
        return ans

# Binary search
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s, e = 0, len(nums) - 1
        while s < e:
            m = (s + e) // 2
            if m % 2:
                m -= 1
            if nums[m] != nums[m + 1]:
                e = m
            else:
                s = m + 2
        return nums[s]
