class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = []
        
        for i in range(m):
            row = [0]*n
                          
            if i==0:
                row = [1]*n
                
                if 1 in obstacleGrid[0]:
                    i = obstacleGrid[0].index(1)
                    row[i:] = [0]*(n-i)
                
            elif obstacleGrid[i][0]!=1:
                row[0] = dp[i-1][0]
                
            dp.append(row)
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]==1:
                    dp[i][j] = 0
                
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]