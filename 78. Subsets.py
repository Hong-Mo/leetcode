class Solution:
    def recursive(self, nums, choose, cur, ans):
        if cur==len(nums):
            ins = []
            
            for i in range(len(nums)):
                if choose[i]:
                    ins.append(nums[i])
            
            ans.append(ins[:])
        
        else:
            choose[cur]=True
            self.recursive(nums, choose, cur+1, ans)
            choose[cur]=False
            self.recursive(nums, choose, cur+1, ans)
            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        choose, ans = [True]*len(nums), []
        self.recursive(nums, choose, 0, ans)
        
        return ans