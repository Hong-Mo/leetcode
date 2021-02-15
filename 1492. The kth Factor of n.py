class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        second_half = []
        p = pow(n, 0.5)
        
        if p%1 == 0:
            p -= 1
        
        for i in range(1, int(p)+1):
            if n%i == 0 :
                second_half.append(n/i)
                k -= 1
            
            if k==0 :
                return i
        
        if p%1 == 0:
            p += 1
            second_half.append(p)
        
        if len(second_half)<k:
            return -1
        
        return int(second_half[-k])