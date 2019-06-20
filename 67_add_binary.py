if __name__ == "__main__":
    a = "1111"
    b = "1111"
    al = [int(i) for i in list(a)]
    bl = [int(i) for i in list(b)]
    while len(al) > len(bl):
        bl.insert(0, 0)
    while len(bl) > len(al):
        al.insert(0, 0)

    ans = []
    t = 0
    for i in range(len(al) - 1, -1, -1):
        if al[i] == bl[i] == 1:
            if t == 1:
                ans.insert(0, 1)
            else:
                ans.insert(0, 0)
                t = 1
        elif al[i] != bl[i]:
            if t == 1:
                ans.insert(0, 0)
            else:
                ans.insert(0, 1)
        else:
            if t == 1:
                ans.insert(0, 1)
                t = 0
            else:
                ans.insert(0, 0)
    if t == 1:
        ans.insert(0, 1)
    answer = [str(i) for i in ans]
    print("".join(answer))
