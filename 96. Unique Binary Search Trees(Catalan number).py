class Solution:
    def stairs(self, n):
        res = 1
        
        for i in range(1, n+1):
            res *= i
        
        return res
         
    def numTrees(self, n: int) -> int:
        ans = (self.stairs((2*n))//pow(self.stairs(n), 2))//(n+1)
        
        return ans