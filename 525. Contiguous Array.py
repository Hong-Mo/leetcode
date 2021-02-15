class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre = {}
        count = ans = 0
        
        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1
            
            else:
                count -= 1
            
            l = 0
            
            if count == 0:
                l = i+1
                
            elif count in pre.keys():
                l = i-pre[count]
            
            else:
                pre[count] = i
            
            ans = max(ans, l)
        
        return ans