class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix and matrix[0]:
            m, row = len(matrix), 0

            while row<m and target>=matrix[row][0]:
                row += 1

            left, right = 0, len(matrix[0])-1
            search = matrix[row-1]

            while left<=right:
                mid = (left+right)//2
                
                if target>search[mid]:
                    left = mid+1
                
                elif target<search[mid]:
                    right = mid-1
                
                else:
                    return True
        
        return False