class Solution:
    def per(self, S, side, index, per):
        if side == index:
            ans = ''
            
            for c in S :
                ans += c
                
            per.append(ans)
        
        for i in range(side, len(S)):
            if S[i].isalpha():
                
                S[i] = S[i].lower()
                self.per(S, i+1, index, per)
                
                
                S[i] = S[i].upper()
                self.per(S, i+1, index, per)
                
                break
                
    def letterCasePermutation(self, S: str) -> List[str]:
        per = []
        S = list(S)
        index = -1
        
        for i in range(len(S)-1, -1, -1):
            if S[i].isalpha():
                index = i+1
                break
        
        self.per(S, 0, index, per)
        
        if len(per)==0 :
            ans = ''
            
            for c in S :
                ans += c
                
            per.append(ans)
        
        
        return per