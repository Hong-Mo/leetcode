class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        ans, dp = 0, [[0]*(len(A)+1) for i in range(len(B)+1)]
        
        for i in range(1, len(B)+1):
            for j in range(1, len(A)+1):
                if B[i-1]==A[j-1]:
                    cur = dp[i-1][j-1]+1
                    dp[i][j], ans = cur, max(ans, cur)
        
        return ans