class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if cnt==1 or ((i+2<len(nums) and nums[i]>nums[i+2]) and\
                              (i-1>=0 and nums[i-1]>nums[i+1])):
                    return False
                
                cnt += 1
        
        return True