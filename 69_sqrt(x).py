if __name__ == "__main__":
    x = 4
    ans = 0
    if x == 1:
        print(1)
    elif x == 0:
        print(0)
    for i in range(int(x / 2) + 1):
        if i * i > x:
            ans = prev
            break
        else:
            prev = i
            ans = prev
    print(ans)
