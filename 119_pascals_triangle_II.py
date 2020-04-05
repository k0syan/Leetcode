class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        retList = []
        for i in range(rowIndex + 1):
            if i == 0:
                retList = [1]
            else:
                curList = []
                # print(retList)
                for j in range(len(retList)):
                    if j == 0:
                        curList.append(retList[j])

                    if j == len(retList) - 1:
                        curList.append(retList[j])
                    else:
                        curList.append(retList[j] + retList[j + 1])
                retList = curList
        return (retList)

# From Pascal's triangle definition

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row
