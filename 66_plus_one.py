if __name__ == "__main__":
    digits = [4,3,2,1]
    x = [str(d) for d in digits]
    a = int("".join(x))
    a += 1
    tmp = list(str(a))
    a = [int(t) for t in tmp]
    print(a)
