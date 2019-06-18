if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = []
    i = 0
    cur = intervals[i]
    m = [cur[0], cur[1]]
    while i < len(intervals) - 1:
        cur = intervals[i]
        nex = intervals[i + 1]
        if i == len(intervals) - 2:
            if m[1] < nex[0]:
                merged.append(m)
                m = [nex[0], nex[1]]
                merged.append(m)
                break
            else:
                if nex[0] <= m[1] < nex[1]:
                    m[1] = nex[1]
            merged.append(m)
            break
        if nex[0] <= m[1] < nex[1]:
            m[1] = nex[1]
            i += 1
        elif m[1] >= nex[1]:
            i += 1
        elif m[1] < nex[0]:
            merged.append(m)
            m = [nex[0], nex[1]]
            i += 1

    print(merged)
