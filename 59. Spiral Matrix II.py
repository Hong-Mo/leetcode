class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        cur, judge, count = 1, 1, pow(n ,2)
        side = [n-1, n-1, 0, 0] # right, bottom, left, top
        ans = []
        
        for i in range(n):
            row = [0]*n
            ans.append(row)
            
        row, col = 0, -1
        
        while cur<=count:
            if judge==1:
                col += 1
                ans[row][col] = cur
                
                if col==side[0]:
                    side[3] += 1
                    judge = 2
                    
            elif judge==2:
                row += 1
                ans[row][col] = cur
                
                if row==side[1]:
                    side[0] -= 1
                    judge = 3
            
            elif judge==3:
                col -= 1
                ans[row][col] = cur
                
                if col==side[2]:
                    side[1] -= 1
                    judge = 4
            
            elif judge==4:
                row -= 1
                ans[row][col] = cur
                
                if row==side[3]:
                    side[2] += 1
                    judge = 1
            
            cur += 1
        
        return ans