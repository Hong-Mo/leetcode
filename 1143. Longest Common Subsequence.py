class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)+1
        l2 = len(text2)+1
        
        dp = []
        
        for i in range(0, l1):
            row = [0]* l2
            dp.append(row)
        
        
        for i in range(1, l1):
            
            for j in range(1, l2):
                
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])  
                
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])  
        
        
        return dp[l1-1][l2-1]