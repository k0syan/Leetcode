nums = []

if len(nums) == 0:
    print(0)
else:
    p = nums[0]
    i = 1
    x = len(nums)
    while i < x:
        c = nums[i]
        # print("i = ", i)
        # print("c = ", c)
        # print("p = ", p)
        if p == c:
            del nums[i]
            x -= 1
            i -= 1
        else:
            p = c
        i += 1
    print(nums)
