class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = []
        
        for i in range(m+1):
            row = [0]*(n+1)
            dp.append(row)
        
        for row in range(1, m+1):
            for col in range(1, n+1):
                if row==1:
                    dp[row][col] = dp[row][col-1]+grid[row-1][col-1]
                
                elif col==1:
                    dp[row][col] = dp[row-1][col]+grid[row-1][col-1]
                
                else:
                    dp[row][col] = min(dp[row-1][col], dp[row][col-1])+grid[row-1][col-1]
        
        return dp[m][n]