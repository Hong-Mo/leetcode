class Solution:
    def recursion(self, cur, s):
        plus, op = 0, 1
        
        while cur[0]<len(s):
            store = ''
            
            if s[cur[0]]=='(':
                cur[0]+=1
                plus += (op*self.recursion(cur, s))
            
            elif s[cur[0]]==')':
                return plus
            
            elif s[cur[0]]=='+' or s[cur[0]]=='-':
                op = 44-ord(s[cur[0]])
            
            while cur[0]<len(s) and s[cur[0]].isdigit():
                store, cur[0] = store+s[cur[0]], cur[0]+1
            
            if store:    
                plus, op, cur[0] = plus+(op*int(store)), 1, cur[0]-1

            cur[0] += 1
        
        return plus
    
    def calculate(self, s: str) -> int:
        return self.recursion([0], s)