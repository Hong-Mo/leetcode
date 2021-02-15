class Solution:
    def decodeString(self, s: str) -> str:
        ans = ''
        s = list(s)
        
        while '[' in s:
            right = 0
            
            while s[right]!=']':
                right += 1
            
            left = right
            
            while s[left]!='[':
                left -= 1
            
            digit = left -1
            
            while digit>=0 and s[digit].isdigit():
                digit -= 1
            
            num = ''
            
            for n in s[digit+1:left]:
                num += n
            
            num = int(num)
            copy = ''
            
            for i in range(left+1, right):
                copy += s[i]
            
            ins = ''
            
            for i in range(0, num):
                ins += copy

            s[right] = ins
            del s[digit+1:right]
        
        for c in s :
            ans += c
        
        return ans