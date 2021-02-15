class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = []
        
        for num in A:
            square = pow(num, 2)
            ans.append(square)
        
        ans.sort()
        
        return ans