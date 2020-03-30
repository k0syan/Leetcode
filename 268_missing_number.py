nums = [3, 0, 1]
n = len(nums)
sn = int(n * (n + 1) / 2)
print(sn)
sm = 0
for a in nums:
    sm += a
print(sn - sm)
