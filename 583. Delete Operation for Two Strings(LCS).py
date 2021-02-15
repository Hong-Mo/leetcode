class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = []
        
        for i in range(len(word1)+1):
            row = [0]*(len(word2)+1)
            dp.append(row)
            
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        ans = (len(word1)+len(word2))-(dp[len(word1)][len(word2)]*2)
        
        return ans