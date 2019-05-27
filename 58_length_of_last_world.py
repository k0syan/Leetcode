if __name__ == "__main__":
    s = input()
    x = s.split()
    if len(x) == 0:
        print(0)
    else:
        print(len(list(x[len(x) - 1])))
