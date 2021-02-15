class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        c = {}
        
        for num in A :
            
            if num in c.keys():
                c[num] += 1
            
            else:
                c.setdefault(num, 1)
        
        c = {value:key for key, value in c.items()}
        
        return c[len(A)/2]