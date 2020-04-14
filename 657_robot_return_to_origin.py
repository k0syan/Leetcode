class Solution:
    def judgeCircle(self, moves: str) -> bool:
        lr = 0
        ud = 0
        for m in moves:
            if m == "L":
                lr += 1
            if m == "R":
                lr -= 1
            if m == "U":
                ud += 1
            if m == "D":
                ud -= 1
        return lr == 0 and ud == 0

    
# One liner
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
