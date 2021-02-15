class Solution:
    def permute(self, per, current, check, left, ans):
        if left==0:
            s = ''
            
            for i in range(0, current):
                s += per[i]
            
            for i in range(current, len(per)):
                s += ')'
            
            ans.append(s)
        else:
        
            if check-1>=0:
                per[current] = ')'
                self.permute(per, current+1, check-1, left, ans)
            
            per[current] = '('
            self.permute(per, current+1, check+1, left-1, ans)
            
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        per = ['(']*(2*n)
        
        self.permute(per, 1, 1, n-1, ans)
        
        return ans