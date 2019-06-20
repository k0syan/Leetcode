if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = -99999999999
    ans = -9999999999
    for n in nums:
        if s > 0:
            s += n
        else:
            s = n
        ans = max(s, ans)
    print(ans)
