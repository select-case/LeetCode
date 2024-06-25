class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        sum_ = 0
        for i in range(len(grid[0])):
            sum_ += grid[0][i]
            dp[0][i] = sum_
        sum_ = 0
        for i in range(len(grid)):
            sum_ += grid[i][0]
            dp[i][0] = sum_
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        print(dp)
        return dp[-1][-1]
        
            