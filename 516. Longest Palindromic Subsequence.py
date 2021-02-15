class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = []
        l = len(s)
        
        for i in range(0, l):
            row = [0]*l
            dp.append(row)
            dp[i][i] = 1
        
        for i in range(1, l):
            for j in range(i-1, -1, -1):
                if s[i]==s[j]:
                    dp[i][j] = dp[i-1][j+1]+2
                
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i-1][j])
        
        return dp[-1][0]

# dp[i][j] = 0, if i<j
# dp[i][j] = 1, if i==j
# dp[i][j] = dp[i-1][j+1]+2, if s[i]== s[j]
# dp[i][j] = max(dp[i][j+1], dp[i-1][j]), if s[i]!=s[j]