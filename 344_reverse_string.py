if __name__ == "__main__":
    s = ["H","a","n","n","a","h"]
    for i in range(int(len(s) / 2)):
        tmp = s[i]
        s[i] = s[len(s) - 1 - i]
        s[len(s) - 1 - i] = tmp
