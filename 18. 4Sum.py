class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()
        
        for i in range(3, len(nums)):
            for j in range(2, i):
                remain = target-(nums[i]+nums[j])
                left, right = 0, j-1
                
                while left<right:
                    plus = nums[left]+nums[right]
                    
                    if plus<remain:
                        left += 1
                    
                    elif plus>remain:
                        right -= 1
                    
                    else:
                        ans.add((nums[left], nums[right], nums[j], nums[i]))
                        left, right = left+1, right-1
                        
                        while left<right and nums[left]==nums[left-1]:
                            left += 1
                        
                        while left<right and nums[right]==nums[right+1]:
                            right -= 1
        
        ans = [list(seq) for seq in ans]
        
        return ans