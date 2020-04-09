class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = w = int(sqrt(area))
        while l * w != area:
            if l * w < area:
                l += 1
            if l * w > area:
                w -= 1
        return (l, w) 
            
