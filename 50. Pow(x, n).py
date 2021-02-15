class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans, base = 1, x
        if n<0:
            n, base= -n, (1/x)
        
        while n>0:
            if n%2==1:
                ans *= base
            
            base = (base*base)
            n >>= 1            
        
        return ans