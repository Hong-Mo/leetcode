class Solution:
    def recurisve(self, nums, cur, ans):
        if (cur==len(nums)) and (nums not in ans):
            ans.append(nums[:])
        
        for i in range(cur, len(nums)):
            if nums[cur]!= nums[i] or cur==i:
                nums[cur], nums[i] = nums[i], nums[cur]
                self.recurisve(nums, cur+1, ans)
                nums[cur], nums[i] = nums[i], nums[cur]
                
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.recurisve(nums, 0, ans)
        
        return ans