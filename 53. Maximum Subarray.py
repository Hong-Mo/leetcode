class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, cur = 0, 0
        
        for num in nums:
            cur = max(0, (cur+num))
            max_sum = max(cur, max_sum)
        
        if max_sum==0:
            max_sum = max(nums)
        
        return max_sum