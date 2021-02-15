class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        ans = [-1, -1]
        
        if not nums:
            return ans
        
        while left<=right:
            mid = (left+right)//2
            
            if nums[mid]<target:
                left = mid+1
            
            elif nums[mid]>target:
                right = mid-1
            
            else:
                break
        
        right_l = left_r = mid
        
        while left<=right_l:
            mid = (left+right_l)//2
            
            if nums[mid]<target:
                left = mid+1
            
            elif nums[mid]>target:
                right_l = mid-1
            
            elif (mid-1)>=0 and nums[mid-1]==target:
                right_l = mid-1
            
            else:
                ans[0] = mid
                break
        
        while left_r<=right:
            mid = (left_r+right)//2
            
            if nums[mid]<target:
                left_r = mid+1
            
            elif nums[mid]>target:
                right = mid-1
            
            elif (mid+1)<len(nums) and nums[mid+1]==target:
                left_r = mid+1
            
            else:
                ans[1] = mid
                break
        
        return ans