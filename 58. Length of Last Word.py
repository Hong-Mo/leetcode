class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        
        count = 0 
        
        while m!=n:
            
            m = m>>1
            n = n>>1
            count+=1
        
        return m<<count

print(Solution.rangeBitwiseAnd(Solution, 5,7))