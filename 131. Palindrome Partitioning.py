class Solution:
    def isPalindrome(self, s):
        l, cur = len(s)//2, -1
        check = list(s[:l])
        
        while check:
            c = check.pop(0)
            
            if c!=s[cur]:
                return False
            
            cur -= 1
        
        return True
    
    def recursion(self, s, cur, part, ans):
        if cur==len(s):
            ins = (part.split('.'))[:-1]
            ans.append(ins)
            
        start = 1
        
        while (cur+start)<=len(s):
            s_par = s[cur:cur+start]
            
            if len(s_par)==1 or self.isPalindrome(s_par):
                self.recursion(s, cur+start, part+s_par+'.', ans)
            
            start += 1
            
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        self.recursion(s, 0, '', ans)
        
        return ans