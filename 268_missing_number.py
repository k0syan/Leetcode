nums = [3, 0, 1]
n = len(nums)
sn = int(n * (n + 1) / 2)
sm = 0
for a in nums:
    sm += a
print(sn - sm)
