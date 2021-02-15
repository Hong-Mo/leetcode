class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_row_sqr = [0]*9
        check_col = [0]*9
        
        for i in range(0, 9):
            for j in range(0, 9):
                
                if board[i][j].isdigit():
                    check_row_sqr[int(board[i][j])-1] += 1
                    
                    if check_row_sqr[int(board[i][j])-1] > 1 :
                        return False
                    
                if board[j][i].isdigit():
                    check_col[int(board[j][i])-1] += 1
                    
                    if check_col[int(board[j][i])-1] > 1:
                        return False
                    
            
            check_row_sqr[:] = [0 for k in range(0,9)]
            check_col[:] = [0 for k in range(0,9)]
        
        row = 0
        col = 0
        
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    for l in range(0, 3):
                        
                        if board[row+k][col+l].isdigit():
                            check_row_sqr[int(board[row+k][col+l])-1] += 1
                        
                            if check_row_sqr[int(board[row+k][col+l])-1] > 1:
                                return False
                
                
                check_row_sqr[:] = [0 for m in range(0,9)]
                col += 3
        
            row += 3
            col  = 0
        
        return True
