def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    pre = 1
    pr = 2
    for i in range(3, n + 1):
        cu = pre + pr
        pre = pr
        pr = cu
    return pr


print(climbStairs(3))
