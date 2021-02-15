class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        dp, max_side = [], 0
        
        for i in range(len(grid)):
            dp.append([])
            
            for j in range(len(grid[i])):
                acc = [0, 0]
                
                if grid[i][j]==1:
                    if i==0:
                        acc[0] = 1
                    else:
                        acc[0] = dp[i-1][j][0]+1
                    
                    if j==0:
                        acc[1] = 1
                    else:
                        acc[1] = dp[i][j-1][1]+1
                    
                    side, max_side = min(acc), max(max_side, 1)
                    
                    for k in range(side, max_side, -1):
                        if dp[i][j-(k-1)][0]>=k and dp[i-(k-1)][j][1]>=k:
                            max_side = k
                            break
                        
                dp[i].append(acc)
        
        return pow(max_side, 2)