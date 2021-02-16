class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans, word, pre = [], s.split(' '), 1
        
        while pre:
            pre, ins = 0, ''
            
            for i in range(len(word)-1, -1, -1):
                if not (pre or word[i]):
                    continue
                
                if word[i]:
                    ins, word[i] = word[i][0]+ins, word[i][1:]
                
                else:
                    ins = ' '+ins
                    
                pre = 1
            
            ans.append(ins)
        
        ans.pop()
        
        return ans