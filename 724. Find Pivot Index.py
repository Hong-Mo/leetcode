class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = 0
        
        for i in range(1, len(nums)):
            right += nums[i]
            
        if (right == left) and (len(nums)!=0)  :
            return 0
        
        for i in range(1, len(nums)):
            left += nums[i-1]
            right -= nums[i]

            if right == left:
                return i
        
        return -1