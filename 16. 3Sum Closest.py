class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ini = sum(nums[:3])
        ans = [ini, abs(ini-target)]
        nums.sort()
        
        for i in range(0, len(nums)):
            check = target - nums[i]
            left, right = 0, i-1
            
            while left<right:
                plus = nums[left]+nums[right]
                dif = check-plus
                
                if dif>0:
                    left += 1
                
                elif dif<0:
                    right -= 1
                
                else:
                    return target
                
                if abs(dif)<ans[1]:
                    ans[:] = nums[i]+plus, abs(dif)
            
        return ans[0]