class Solution:
    def reverseWords(self, s: str) -> str:
        cur, stk, ans = 0 ,[], ''
        
        while cur<len(s):
            word = ''
            
            while cur<len(s) and s[cur]==' ':
                cur += 1
            
            while cur<len(s) and s[cur]!=' ':
                word += s[cur]
                cur += 1
            
            if len(word)>0:
                stk.append(word)

        while stk:
            ans += stk.pop()+' '
        
        return ans[:-1]