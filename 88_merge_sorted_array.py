nums1 = [0]
m = 0
nums2 = [2]
n = 1

# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3

j = 0
i = 0
om = m
if len(nums2) == 0:
    print(nums1)
while i < len(nums1):
    n1 = nums1[i]
    n2 = nums2[j]
    if n1 < n2:
        if i >= om:
            nums1.insert(i, n2)
            om += 1
            j += 1
            if j == n:
                break
        i += 1
    else:
        nums1.insert(i, n2)
        om += 1
        j += 1
        if j == n:
            break
        i += 1

for i in range(n):
    nums1.pop()
print(nums1)
