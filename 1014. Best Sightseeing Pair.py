class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = plus = 0
        
        for num in A:
            res = max(res, plus+num)
            plus = max(plus, num)-1
        
        return res