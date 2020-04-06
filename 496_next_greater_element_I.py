class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        retArr = []
        for n in nums1:
            i = nums2.index(n)
            for j in range(i, len(nums2)):
                x = nums2[j]
                if x > n:
                    retArr.append(x)
                    break
                else:
                    if j == len(nums2) - 1:
                        retArr.append(-1)
        return retArr      
