class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        l = len(palindrome)
        
        if l > 1:
            
            palindrome = list(palindrome)
            
            for i in range(0, l//2):

               if palindrome[i] != 'a':
                   palindrome[i] = 'a'
                   return ''.join(palindrome)

            palindrome[-1] = 'b'
            return ''.join(palindrome)
                
        return ''