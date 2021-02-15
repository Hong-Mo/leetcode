class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        palindrome = list(palindrome)
        l = len(palindrome)
        bound = l//2
        
        for i in range(0, bound):
            
            asi = ord(palindrome[i]) - 1
            
            if asi >= 97  :
                palindrome[i] = chr(97)
                return ''.join(palindrome)
        
        if l%2 == 0:
            bound -= 1
        
        for i in range(l-1, bound, -1):
            asi = ord(palindrome[i]) + 1 
            
            if asi <= 122 :
                palindrome[i] = chr(asi)
                return ''.join(palindrome)
                
        return ''

print(Solution.breakPalindrome(Solution, 'zzzz'))