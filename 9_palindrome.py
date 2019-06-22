if __name__ == "__main__":
    x = -121
    t = True
    if list(str(x))[0] == "-":
        t = False
    else:
        xl = [int(i) for i in list(str(x))]
        for i in range(int(len(xl) / 2) + 1):
            if xl[i] != xl[len(xl) - i - 1]:
                t = False
                break
    print(t)
