from typing import List

def generate(numRows: int) -> List[List[int]]:
    retList = []
    for i in range(numRows):
        if i == 0:
            retList.append([1])
        else:
            # print(i)
            # print(retList)
            prList = retList[i - 1]
            curList = []
            # print(retList)
            for j in range(len(prList)):
                if j == 0:
                    curList.append(prList[j])

                if j == len(prList) - 1:
                    curList.append(prList[j])
                else:
                    curList.append(prList[j] + prList[j + 1])
            retList.append(curList)
    return (retList)


print(generate(5))