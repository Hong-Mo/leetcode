class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        step, count = len(matrix), pow(len(matrix), 2)
        start, judge = 0, -1
        
        while count>0:
            index = start+step-1
            
            if judge==-1:
                store = matrix[start][start:index+1]
                judge = 0
            
            elif judge==0:
                j = 0
                
                for i in range(start, index+1):
                    store[j], matrix[i][index] = matrix[i][index], store[j]
                    j += 1
                
                judge, count = 1, count-step
            
            elif judge==1:
                j = 1
                
                for i in range(index-1, start-1, -1):
                    store[j], matrix[index][i] = matrix[index][i], store[j]
                    j += 1
                
                judge, count = 2, count-(step-1)
                
            elif judge==2:
                j = 1
                
                for i in range(index-1, start-1, -1):
                    store[j], matrix[i][start] = matrix[i][start], store[j]
                    j += 1
                
                judge, count = 3, count-(step-1)
            
            elif judge==3:
                j = 1
                
                for i in range(start+1, index):
                    store[j], matrix[start][i] = matrix[start][i], store[j]
                    j += 1
                
                judge, count = -1, count-(step-2)
                start, step = start+1, step-2