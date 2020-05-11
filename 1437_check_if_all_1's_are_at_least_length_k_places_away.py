class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        c = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if c == -1:
                    c = i
                else:
                    if i - c <= k:
                        return False
                    else:
                        c = i
        return True
