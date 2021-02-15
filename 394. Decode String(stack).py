class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        
        for c in s :
            
            if c != ']':
                stk.append(c)
            
            else:
                store = []
                repeat = ''
                
                while not stk[-1].isdigit():
                    top = stk.pop()
                    
                    if top != '[' and top != ']':
                        store.append(top)
                
                while store:
                    repeat += store.pop()
                    
                times = ''
                
                while stk and stk[-1].isdigit():
                    top = stk.pop()
                    times += top
                
                times = int(times[::-1])
                ins = ''
                
                for i in range(0, times):
                    ins += repeat
                    
                stk.append(ins)

        ans = ''
        
        for l in stk:
            ans += l
        
        return ans