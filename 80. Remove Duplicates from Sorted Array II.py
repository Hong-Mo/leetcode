class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count, cur = 1, 1
        
        while cur<len(nums):
            if nums[cur]==nums[cur-1]:
                count += 1
            
            else:
                count = 1
            
            if count>2:
                del nums[cur]
                count, cur = count-1, cur-1
            
            cur += 1
        
        return len(nums)