class Solution:
    def makeGood(self, s: str) -> str:
        cur = 0
        
        while cur<len(s)-1:
            if cur>=0 and ((s[cur].islower() and s[cur+1].isupper()) or\
               (s[cur].isupper() and s[cur+1].islower())) and\
               (s[cur].lower()==s[cur+1].lower()):
                   s = s[:cur]+s[cur+2:]
                   cur -= 2
            
            cur += 1
        
        return s