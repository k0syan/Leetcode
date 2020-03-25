roman = list(input())
ans = []
curNum = 0
r = roman[0]
if len(roman) > 1:
    rn = roman[1]
else:
    rn = ""
i = 0
while i < len(roman):
    skipNext = False
    if r == "I":
        if rn == "V":
            curNum += 4
            skipNext = True
        elif rn == "X":
            curNum += 9
            skipNext = True
        else:
            curNum += 1
    elif r == "V":
        curNum += 5
    elif r == "X":
        if rn == "L":
            curNum += 40
            skipNext = True
        elif rn == "C":
            curNum += 90
            skipNext = True
        else:
            curNum += 10
    elif r == "L":
        curNum += 50
    elif r == "C":
        if rn == "D":
            curNum += 400
            skipNext = True
        elif rn == "M":
            curNum += 900
            skipNext = True
        else:
            curNum += 100
    elif r == "D":
        curNum += 500
    elif r == "M":
        curNum += 1000
    i += 1
    if i == len(roman):
        break
    if skipNext:
        i += 1
        if i == len(roman):
            break
        r = roman[i]
        if i < len(roman) - 1:
            rn = roman[i + 1]
        else:
            rn = ""
    else:
        r = roman[i]
        if i < len(roman) - 1:
            rn = roman[i + 1]
        else:
            rn = ""
print(curNum)
