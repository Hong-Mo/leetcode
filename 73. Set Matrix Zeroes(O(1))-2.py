class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m ,n = len(matrix), len(matrix[0])
        first_row = first_col = False
        
        for i in range(n):
            if matrix[0][i] == 0:
                first_row = True
        
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for j in range(1, n):
            if matrix[0][j]==0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        for i in range(1, m):
            if matrix[i][0]==0:
                matrix[i][:] = [0]*n
        
        if first_row:
            matrix[0][:] = [0]*n
        
        if first_col:
            for j in range(0, m):
                matrix[j][0] = 0