class Solution:
    def numDecodings(self, s: str) -> int:
        count = [1]*(len(s)+1)
        
        if s[0]<'1':
            return 0
        
        for i in range(1, len(s)):
            if s[i-1]+s[i]<='26' and s[i-1]+s[i]>='1':
                if s[i]>'0':
                    count[i+1] = count[i]+count[i-1]
                
                else:
                    count[i+1] = count[i-1]
            
            elif s[i]<'1':
                return 0
            
            else:
                count[i+1] = count[i]
        
        return count[-1]