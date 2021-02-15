class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 :
            return []
        
        side = [0, len(matrix[0])-1, 0, len(matrix)-1] # left, right, top, bottom
        judge = i = 0
        j = -1
        num = len(matrix[0]) * len(matrix)
        ans = []
        
        while num > 0 :
            if judge == 0 :
                j += 1
                ans.append(matrix[i][j])
                
                if j == side[1] :
                    side[2] += 1
                    judge = 1
                    
            
            elif judge == 1 :
                i += 1
                ans.append(matrix[i][j])
                
                if i == side[3] :
                    side[1] -= 1
                    judge = 2
            
            elif judge == 2 :
                j -= 1
                ans.append(matrix[i][j])
                
                if j == side[0] :
                    side[3] -= 1
                    judge = 3
            
            elif judge == 3 :
                i -= 1
                ans.append(matrix[i][j])
                
                if i == side[2] :
                    side[0] += 1
                    judge = 0
            
            num -= 1
        
        return ans