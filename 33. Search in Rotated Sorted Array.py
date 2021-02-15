class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left<=right:
            mid = (left+right)//2
            
            if target<nums[mid]:
                if nums[left]>nums[mid] or nums[left]<=target:
                    right = mid-1
                
                else:
                    left = mid+1
            
            elif target>nums[mid]: 
                if nums[right]<nums[mid] or nums[right]>=target :
                    left = mid+1
                
                else:
                    right = mid-1
            
            else:
                return mid

        return -1