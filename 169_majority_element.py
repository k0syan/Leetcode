class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        max_count = max(d.values())
        print(max_count)
        key = [k for k, v in d.items() if v == max_count]
        return(key[0])
            
        
# Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
