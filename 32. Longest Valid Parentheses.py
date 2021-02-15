class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        ans = accumulate = 0
        
        for c in s:
            if c == '(':
                stk.append(0)
            
            elif len(stk)>1:
                stk[len(stk)-2] += (stk.pop()+2)
            
            elif stk:
                accumulate += (stk.pop()+2)
            
            else:
                ans, accumulate = max(ans, accumulate), 0
            
        stk.append(accumulate)
            
        return max(ans, max(stk))