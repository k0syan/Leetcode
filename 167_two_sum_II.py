numbers = [2, 7, 11, 15]
target = 9

d = {}
for i, n in enumerate(numbers):
    m = target - n
    if m in d:
        print([d[m] + 1, i + 1])
        break
    else:
        d[n] = i
