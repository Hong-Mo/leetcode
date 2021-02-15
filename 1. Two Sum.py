class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(i, num) for i, num in enumerate(nums)]
        nums = sorted(nums, key = lambda x:x[1])
        left, right = 0, len(nums)-1
        
        while left<right:
            i, num_l = nums[left]
            j, num_r = nums[right]
            
            if num_l+num_r>target:
                right -= 1
            
            elif num_l+num_r<target:
                left += 1
            
            else:
                return sorted([i, j])