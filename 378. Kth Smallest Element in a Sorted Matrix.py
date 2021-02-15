class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        nums = []
        
        for row in matrix :
            for num in row :
                nums.append(num)
                
        nums.sort()
                
        return nums[k-1]