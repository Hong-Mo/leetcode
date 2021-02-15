class Solution:
    def binary_search(self, left, right, nums, target, ans):
        while left<=right and (not ans[0]):
            mid = (left+right)//2
            
            if nums[mid]>target:
                if target>=nums[left] or nums[left]>nums[mid]:
                    right = mid-1
                
                elif nums[left]==nums[mid]:
                    self.binary_search(mid+1, right, nums, target, ans)
                    self.binary_search(left, mid-1, nums, target, ans)
                    break
                
                else:
                    left = mid+1
                
            elif nums[mid]<target:
                if target<=nums[right] or nums[right]<nums[mid]:
                    left = mid+1
                
                elif nums[right]==nums[mid]:
                    self.binary_search(mid+1, right, nums, target, ans)
                    self.binary_search(left, mid-1, nums, target, ans)
                    break
                    
                else:
                    right = mid-1
            
            else:
                ans[0] = True
                break
                
    def search(self, nums: List[int], target: int) -> bool:
        ans = [False]
        self.binary_search(0, len(nums)-1, nums, target, ans)
        
        return ans[0]