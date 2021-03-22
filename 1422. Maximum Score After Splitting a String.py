class Solution:
    def maxScore(self, s: str) -> int:
        ans, score = 0, s.count('1')
        
        for i in range(len(s)-1):
            if s[i]=='0':
                score += 1
            
            else:
                score -= 1
            
            ans = max(ans, score)
        
        return ans