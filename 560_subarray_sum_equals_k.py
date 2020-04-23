class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mem = {}
        ans = s = 0
        for n in nums:
            s += n
            cmp = s - k
            if cmp == 0:
                ans += 1
            if cmp in mem:
                ans += mem[cmp]
            if s in mem:
                mem[s] = mem[s] + 1
            else:
                mem[s] = 1
        return ans
