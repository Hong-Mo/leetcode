class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col]==0:
                    for i in range(n):
                        if matrix[row][i]!=0:
                            matrix[row][i] = '0'
                    
                    for i in range(m):
                        if matrix[i][col]!=0:
                            matrix[i][col] = '0'
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col]=='0':
                    matrix[row][col] = 0