class Solution(object):
    def maxAreaOfIsland(self, grid):

        def dfs(grid , row , col) :
            if row<0 or col<0 or row==len(grid) or col==len(grid[row]) or grid[row][col]==0: return 0 
            grid[row][col]=0 
            return (1+dfs(grid,row+1,col)+dfs(grid,row-1,col)+dfs(grid,row,col+1)+dfs(grid,row,col-1)) 
        n = len(grid) 
        m = len(grid[0]) 
        mn = 0
        for i in range(n) : 
            for j in range(m) :
                if grid[i][j] == 1 : mn = max(mn , dfs(grid , i , j)) 
        return mn 