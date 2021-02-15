class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        if num <= 1:
            return False
        
        s = 1
        
        for i in range(2, int(pow(num, 0.5))+1):
            if num % i == 0:
                s += (i + (num/i) )
        
        if s == num :
            return True
        
        return False