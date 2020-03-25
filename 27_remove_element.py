nums = [3, 2, 2, 3]
val = 3


if len(nums) == 0:
    print(0)
else:
    i = 0
    x = len(nums)
    while i < x:
        c = nums[i]
        if c == val:
            del nums[i]
            i -= 1
            x -= 1
        i += 1
    print(nums)

