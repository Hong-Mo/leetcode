class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = ['']
        l = 1
        
        for i in range(0, len(S)):
            if S[i].isalpha():
                
                for j in range(0, l):
                    d = ans[0]
                    
                    lower = S[i].lower()
                    ans.append(d+S[len(d):i]+lower)
                    
                    upper = S[i].upper()
                    ans.append(d+S[len(d):i]+upper)

                    del ans[0]
                
                l *= 2
        
        side = len(ans[0])
        
        for i in range(0, len(ans)):
            ans[i] += S[side:]
    
        return ans