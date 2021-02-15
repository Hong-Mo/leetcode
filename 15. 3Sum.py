class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        
        for i in range(0, len(nums)):
            target = -nums[i]
            left, right = 0, i-1
            
            while left<right:
                plus = nums[left]+nums[right]
                
                if plus>target:
                    right -= 1
                
                elif plus<target:
                    left += 1
                
                else:
                    ins = (nums[left], nums[right], nums[i])
                    ans.add(ins)
                    left, right = left+1, right-1
                    
                    while left<right and nums[left]==nums[left-1]:
                        left += 1
                    
                    while left<right and nums[right]==nums[right+1]:
                        right -= 1
                    
        ans = [list(s) for s in ans]
        
        return ans