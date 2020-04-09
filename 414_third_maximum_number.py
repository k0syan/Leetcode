class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m = [-float('inf'), -float('inf'), -float('inf')]
        for n in nums:
            if n in m:
                continue
            if n > m[0]:   
                m = [n, m[0], m[1]]
            elif n > m[1]: 
                m = [m[0], n, m[1]]
            elif n > m[2]: 
                m = [m[0], m[1], n]
        if -float('inf') in m:
            return max(nums)
        return m[2]
