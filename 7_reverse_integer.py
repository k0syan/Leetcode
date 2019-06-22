if __name__ == "__main__":
    x = 1534236469
    m = False
    if x < 0:
        m = True
        x = x * -1
    ans = 0
    while x != 0:
        ans = ans * 10 + int(x % 10)
        x = int(x / 10)
    if m:
        ans = -1 * ans

    if ans < -2147483648 or ans > 2147483647:
        ans = 0

    print(ans)
