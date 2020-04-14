class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        for o in ops:
            if o == "C":
                if len(scores):
                    scores = scores[:-1]
            elif o == "D":
                if len(scores):
                    scores.append(int(scores[-1] * 2))
            elif o == "+":
                if len(scores) > 1:
                    scores.append(int(scores[-1] + scores[-2]))
            else:
                scores.append(int(o))
        return sum(scores)
