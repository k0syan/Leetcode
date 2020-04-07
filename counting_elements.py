class Solution:
    def countElements(self, arr: List[int]) -> int:
        tot = 0
        tmp = 1
        arr.sort()
        for i in range(len(arr) - 1):
            c = arr[i]
            n = arr[i + 1]
            if c == n:
                tmp += 1
            else:
                if c + 1 == n:
                    tot += tmp
                tmp = 1
        return tot
                
