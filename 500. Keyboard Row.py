class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
               ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
               ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
        
        ans = []
        
        for s in words:
            
            ans.append(s)
            low_s = s.lower()
            
            for i in range(0, 3):
                if low_s[0] in row[i]:
                    judge = i 
                    break
            
            for i in range(1, len(low_s)):
                if low_s[i] not in row[judge]:
                    ans.pop()
                    break
        
        return ans