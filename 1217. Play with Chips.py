class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odd = even = 0
        
        for num in chips:
            if num%2 == 0:
                even += 1
            
            else:
                odd += 1
        
        cost = min(even, odd)
        
        return cost