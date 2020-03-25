strs = ["aa","a"]
pref = ""
i = 0
if len(strs) != 0:
    while True:
        br = False
        curL = ""
        for a in strs:
            if i < len(a):
                l = a[i]
            else:
                curL = ""
                br = True
                break
            if curL == "":
                curL = l
            elif curL != l:
                curL = ""
                br = True
                break
        pref += curL
        if br:
            break
        i += 1
print(pref)
