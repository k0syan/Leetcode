nums = [2, 7, 11, 15]
target = 9

d = {}
ans = []
for i, n in enumerate(nums):
    m = target - n
    if m in d:
        ans = [d[m], i]
        break
    else:
        d[n] = i
print(ans)
