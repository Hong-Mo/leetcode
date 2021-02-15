class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        cur, digit, s, ans = 1, len(str(low)), str(low), []
        
        if ord(s[0])+digit-1<=57:
            digit, cur = digit-1, int(s[0])
        
        ini, tail, increment = '1', cur+1, 1
        
        for i in range(digit):
            cur, increment, ini = cur*10+tail, increment*10+1, ini+chr(ord(ini[-1])+1)
            tail += 1
        
        while cur<=high:
            if cur>=low:
                ans.append(cur)
                
            s = str(cur)
            
            if ord(s[-1])==57:
                if ord(s[0])==49:
                    break
                
                ini = ini+chr(ord(ini[-1])+1)
                cur, increment = int(ini), increment*10+1
            
            else:
                cur += increment
        
        return ans