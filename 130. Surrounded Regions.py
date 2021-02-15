class Solution:
    def solve(self, board: List[List[str]]) -> None:
        check = []
        
        for i in range(0, len(board)):
            row = [0]*len(board[0])
            check.append(row)
        
        judge = i = 0
        j = -1
        
        while board:
            if judge == 0 :
                j += 1 
                
                if j==len(board[0])-1:
                    judge = 1
            
            elif judge == 1:
                i += 1
                
                if i==len(board)-1:
                    judge = 2
            
            elif judge == 2 :
                j -= 1
                
                if j==0:
                    judge = 3
            
            elif judge == 3 :
                i -= 1
                
                if i==0:
                    break
            
            stk = []
           
            try:
                if check[i][j] == 0 and board[i][j] == 'O':
                    check[i][j] = 1
                    stk.append([i, j])
            
            except:
                break
            
            while stk:
                coor = stk.pop()
                row, col = coor[0], coor[1]
                
                if col+1<len(board[0]) and board[row][col+1]=='O' and check[row][col+1]==0 :
                    stk.append([row, col+1])
                    check[row][col+1] = 1
                
                if row+1<len(board) and board[row+1][col] == 'O'  and check[row+1][col]==0:
                    stk.append([row+1, col])
                    check[row+1][col] = 1
                
                
                if col-1>=0 and board[row][col-1] == 'O' and check[row][col-1]==0:
                    stk.append([row, col-1])
                    check[row][col-1] = 1
                
                if row-1>=0 and board[row-1][col] == 'O' and check[row-1][col]==0:
                    stk.append([row-1, col])
                    check[row-1][col] = 1
                
                if i==3 and j==8:
                    print(stk)
            
        for i in range(0, len(check)):
            for j in range(0, len(check[i])):
                if check[i][j] == 0:
                    board[i][j] = 'X'