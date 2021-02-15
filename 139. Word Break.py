class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        end = [False]*len(s)
        
        for i in range(len(s)):
            for word in wordDict:
                if word == s[i-len(word)+1:i+1] and (end[i-len(word)] or i-len(word)==-1):
                    end[i] = True
        
        return end[-1]