class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        index = sorted(range(len(A)), key = lambda i:A[i])
        min_index, ans = len(index)-1, 0
        
        for i in index:
            min_index = min(min_index, i)
            
            ans = max((i-min_index), ans)
        
        return ans