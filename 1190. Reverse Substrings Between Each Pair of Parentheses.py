class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        
        for c in s:
            if c!=')':
                stk.append(c)
            
            else:
                store = []
                
                while stk[-1]!='(':
                    store.append(stk.pop())
                
                stk.pop();stk.extend(store)
        
        return ''.join(stk)