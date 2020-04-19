class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        n = len(nums)
        lo, hi = 0, n - 1
        
        while lo < hi:
            mi = (lo + hi) // 2
            if nums[mi] > nums[hi]:
                lo = mi + 1
            else:
                hi = mi
        rp = lo
        lo = 0
        hi = n - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            romi = (mi + rp) % n
            if nums[romi] == target:
                return romi
            if nums[romi] < target:
                lo = mi + 1
            else:
                hi = mi - 1
        return -1
            
            
