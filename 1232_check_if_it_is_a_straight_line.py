class Solution:
    def isColinear(self, x1, y1, x2, y2, x3, y3) -> bool:
        return x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) == 0
    
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n <= 2:
            return True
        for i in range(n - 2):
            cur = coordinates[i]
            nex = coordinates[i + 1]
            nnex = coordinates[i + 2]
            if not self.isColinear(cur[0], cur[1], nex[0], nex[1], nnex[0], nnex[1]):
                return False
        return True
