class Solution:
    def maximum69Number (self, num: int) -> int:
        sNum = str(num)
        for i in range(len(sNum)):
            if sNum[i] == "6":
                arr = list(sNum)
                arr[i] = "9"
                sNum = "".join(arr)
                break
        return int(sNum)
        
