class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        col = image[sr][sc]
        w, l = len(image), len(image[0])
        if col == newColor:
            return image
        def dfs(i, j):
            if image[i][j] == col:
                image[i][j] = newColor
                if i >= 1: dfs(i-1, j)
                if i+1 < w: dfs(i+1, j)
                if j >= 1: dfs(i, j-1)
                if j+1 < l: dfs(i, j+1)
        dfs(sr, sc)
        return image
