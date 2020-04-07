class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        retList = []
        for i in range(1, n + 1):
            if i % 3 == 0:
                if i % 5 == 0:
                    retList.append("FizzBuzz")
                else:
                    retList.append("Fizz")
            elif i % 5 == 0:
                retList.append("Buzz")
            else:
                retList.append(str(i))
        return(retList)
