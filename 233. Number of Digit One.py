class Solution:
    def countDigitOne(self, n: int) -> int:
        ans, bound, base = 0, 10, 1
        num = [base]
        
        while n>=(bound*10):
            bound, base = (bound*10), (base*10)+bound
            num.append(base)

        while bound>1:
            quo, n = divmod(n, bound)
            ans += (quo*num.pop())
            
            if quo>1:
                ans += bound
            
            elif quo==1:
                ans += (n+1)
            
            bound //= 10
        
        if n>0:
            ans += 1
        
        return ans