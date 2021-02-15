class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = 0
        odd = 1
        half_ans = ''
        
        for i in range(0, len(s)):
            
            j = i-1 # odd number palindrome
            k = i+1
            
            count = 1
            pal = s[i]
            
            while (j>=0 and k<len(s)) and (s[j] == s[k]):
                pal += s[k]
                count += 2 
                j -= 1
                k += 1
                
            if count > m :
                m = count 
                half_ans = pal
                odd = 1
            
            j = i-1 # even number palindrome 
            k = i+1
            count = 1
            pal = s[i]
            
            if k<len(s) and s[k] == s[i] :
                k += 1
                count += 1
            

            while (j>=0 and k<len(s)) and (s[j] == s[k]):
                pal += s[k]
                count += 2 
                j -= 1
                k += 1
            
            if count > m :
                m = count 
                half_ans = pal
                odd = 0
            
            
        ans = ''
        
        if odd == 1:
            
            for i in range(len(half_ans)-1, 0, -1):
                ans += half_ans[i]
        
        else:
            
            for i in range(len(half_ans)-1, -1, -1):
                ans += half_ans[i]
        
        ans += half_ans

        return ans   