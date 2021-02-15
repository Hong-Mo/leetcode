class Solution:
    def nextGreaterElement(self, n: int) -> int:
        store = []
        
        while n>0:
            store.insert(0, n%10)
            n //= 10
        
        l = len(store)-1
        
        for i in range(l-1, -1, -1):
            
            for j in range(l, i, -1):
                if store[j]>store[i]:
                    store[j], store[i] = store[i], store[j]
                    min_arr = store[i+1:]
                    min_arr.sort()
                    store[i+1:] = min_arr
                    
                    ans = 0
                    base = 1
                    
                    while store:
                        num = store.pop()
                        ans += (num*base)
                        base *= 10
                    
                    if ans>2147483647:
                        return -1
                    
                    return ans
        
        return -1