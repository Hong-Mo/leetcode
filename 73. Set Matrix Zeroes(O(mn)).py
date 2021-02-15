class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        stk = []
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col]==0:
                    stk.append((row, col))
        
        while stk:
            row, col = stk.pop()
            matrix[row][:] = [0]*len(matrix[row])
            
            for i in range(0, len(matrix)):
                matrix[i][col] = 0