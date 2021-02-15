class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        while len(bits)>1:
            if bits[0] == 1:
                del bits[0:2]
            
            else:
                del bits[0]
        
        if bits:
            return True
        
        return False