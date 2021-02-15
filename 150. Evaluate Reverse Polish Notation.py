class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        
        for s in tokens:
            try:
                stk.append(int(s))
            
            except:
                b = stk.pop()
                a = stk.pop()
                
                if s=='+':
                    stk.append(a+b)
                
                elif s=='-':
                    stk.append(a-b)
                
                elif s=='*':
                    stk.append(a*b)
                
                else:
                    stk.append(int(a/b))
        
        return stk.pop()