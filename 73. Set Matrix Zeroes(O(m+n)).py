class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m ,n = len(matrix), len(matrix[0])
        row, col = [0]*m, [0]*n
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row[i], col[j] = 1, 1
        
        for i in range(m):
            if row[i]==1:
                matrix[i][:] = [0]*len(matrix[0])
        
        for j in range(n):
            if col[j]==1:
                for i in range(m):
                    matrix[i][j] = 0 