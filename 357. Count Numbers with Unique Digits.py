class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans = 1
        
        for i in range(1, n+1):
            store, mul = 9, 9
            
            for j in range(i-2):
                store *= (mul-1)
                mul -= 1
            
            if i>2:
                ans += (store*(i-2))
            
            if i>1:
                store *= mul
                
            ans += store
        
        return ans