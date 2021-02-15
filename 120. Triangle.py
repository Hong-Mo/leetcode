class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for i in range(len(triangle)-2, -1, -1):
            row_above = triangle[i]
            row_below = triangle[i+1]
            
            for j in range(len(row_above)):
                row_above[j] = min(row_below[j], row_below[j+1])+row_above[j]
        
        return triangle[0][0]