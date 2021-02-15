class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix and matrix[0]:
            m, row = len(matrix), 0

            while row<m and target>=matrix[row][0]:
                row += 1

            row -= 1

            if target in matrix[row]:
                return True
        
        return False