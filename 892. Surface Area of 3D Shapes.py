class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        count_area = 0
        count_overlap = 0
        
        for i in range(0, len(grid)):
            
            for j in range(0, len(grid[i])):
                
                if grid[i][j]!= 0 :
                    count_area += grid[i][j]
                    count_overlap += max(grid[i][j]-1, 0)

                    if i-1 >=0 and grid[i-1][j] != 0:
                        count_overlap += min(grid[i][j], grid[i-1][j])

                    if j-1 >= 0 and grid[i][j-1] != 0:
                        count_overlap += min(grid[i][j], grid[i][j-1])

        
        return (6*count_area) - (2*count_overlap)