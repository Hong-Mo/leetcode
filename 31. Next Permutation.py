class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index = None
        
        for i in range(len(nums)-2, -1, -1):
            min_num = max(nums[i+1:])
            
            for j, num in enumerate(nums[i+1:]):
                if num>nums[i] and num<=min_num:
                    min_num, index = num, (j+i+1)
            
            if index:
                nums[i], nums[index] = nums[index], nums[i]
                nums[i+1:] = sorted(nums[i+1:])
                break
        
        if not index:
            nums.sort()