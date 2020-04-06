class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = list(set(nums1) & set(nums2))
        for j in range(len(inter)):
            i = inter[j]
            c1 = nums2.count(i) - 1
            c2 = nums1.count(i) - 1
            c = 0
            if c1 < c2:
                c = c1
            else:
                c = c2
            while c != 0:
                inter.append(i)
                c -= 1
        return(inter)
