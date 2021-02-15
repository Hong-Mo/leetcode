class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        check = [0, 0] #lower, upper
        
        for c in word:
            if c.islower():
                check[0] += 1
                
                if check[1]>1:
                    return False
            
            else:
                check[1] += 1
                
                if check[0]>0:
                    return False
            
        return True