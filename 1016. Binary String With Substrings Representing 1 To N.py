class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(1, N+1):
            b = bin(i)
            
            if b[2:] not in S:
                return False
        
        return True