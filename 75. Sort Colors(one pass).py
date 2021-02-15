class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cur, left, right = 0, -1, len(nums)
        
        while cur<right:
            if nums[cur]==0:
                left += 1
                nums[left], nums[cur] = nums[cur], nums[left]
            
            elif nums[cur]==2:
                right -= 1
                nums[right], nums[cur] = nums[cur], nums[right]
                cur -= 1
            
            cur += 1