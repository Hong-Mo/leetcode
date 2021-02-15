class Solution:
    def DFS(self, word, board, choose, cur, pos, ans):
        if cur==len(word)-1:
            ans[0] = True
        
        elif (not ans[0]):
            r, c = pos
            
            if r>0 and board[r-1][c]==word[cur+1] and (not choose[r-1][c]):
                choose[r-1][c] = True
                self.DFS(word, board, choose, cur+1, (r-1, c), ans)
                choose[r-1][c] = False
            
            if c>0 and board[r][c-1]==word[cur+1] and (not choose[r][c-1]):
                choose[r][c-1] = True
                self.DFS(word, board, choose, cur+1, (r, c-1), ans)
                choose[r][c-1] = False
            
            if r<len(board)-1 and board[r+1][c]==word[cur+1] and (not choose[r+1][c]):
                choose[r+1][c] = True
                self.DFS(word, board, choose, cur+1, (r+1, c), ans)
                choose[r+1][c] = False
            
            if c<len(board[r])-1 and board[r][c+1]==word[cur+1] and (not choose[r][c+1]):
                choose[r][c+1] = True
                self.DFS(word, board, choose, cur+1, (r, c+1), ans)
                choose[r][c+1] = False
                
    def exist(self, board: List[List[str]], word: str) -> bool:
        choose, ans = [], [False]
        
        for i in range(len(board)):
            row = [False]*len(board[i])
            choose.append(row)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    choose[i][j] = True
                    self.DFS(word, board, choose, 0, (i, j), ans)
                    choose[i][j] = False
        
        return ans[0]