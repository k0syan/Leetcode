class Solution:
    def dfs(gr: List[List[str]], d, v):
        diag = vert = False
        if d < 0 or d >= len(gr):
            diag = True
        if v < 0 or v >= len(gr[0]):
            vert = True
        
        if diag or vert or gr[d][v] != "1":
            return
        
        gr[d][v] = "2"
        Solution.dfs(gr, d - 1, v)
        Solution.dfs(gr, d, v - 1)
        Solution.dfs(gr, d + 1, v)
        Solution.dfs(gr, d, v + 1)
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    Solution.dfs(grid, i, j)
                    res += 1
        return res
            
