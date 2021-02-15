class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        N = list(str(N))
        pos, ans = len(N), ''
        
        for i in range(len(N)-1, 0, -1):
            if N[i-1]>N[i]:
                pos = i
                N[i-1] = str(int(N[i-1])-1)
        
        for i in range(0, pos):
            ans += N[i]
        
        for i in range(pos, len(N)):
            ans += '9'
        
        return int(ans)