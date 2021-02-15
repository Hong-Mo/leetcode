class Solution:
    def isUgly(self, num: int) -> bool:
        
        factor = [2, 3, 5]
        
        if num == 0 :
            return False
        
        for f in factor:
            while num % f == 0:
                num = num/f
        
        if num != 1:
            return False
        
        return True