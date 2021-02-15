class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0]*2 # 0: five, 1:ten
        
        for money in bills :
            
            if money == 5 :
                change[0] += 1
            
            elif money == 10 :
                change[0] -= 1
                change[1] += 1
            
            else:
                if change[1] > 0 :
                    change[0] -= 1
                    change[1] -= 1
                
                else:
                    change[0] -= 3
            
            if change[0]<0 :
                return False
        
        return True