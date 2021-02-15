class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        
        while i<len(nums):
            cur = nums[i]
            
            while (cur>0 and cur<=len(nums)) and cur!=nums[cur-1] and cur-1!=i:
                nums[cur-1], cur = cur, nums[cur-1]

            nums[i] = cur
            i += 1

                
        for i, n in enumerate(nums):
            if n!=i+1:
                return i+1
        
        return len(nums)+1