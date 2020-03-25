nums = [1, 3, 5, 6]
target = 7

ans = 0
for i in range(len(nums)):
    n = nums[i]
    if target <= n:
        ans = i
        break
    if target > n and i == len(nums) - 1:
        ans = i + 1
print(ans)
