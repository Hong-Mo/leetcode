class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        dif = max(A)-min(A)
        
        return max(0, dif-(2*K))