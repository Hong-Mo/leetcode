class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        count = 0
        num = len(B)//len(A) + 2
        s = ''
        
        while B not in s  and count < num:
            s += A
            count += 1
            
        if B not in s :
            return -1
        
        return count