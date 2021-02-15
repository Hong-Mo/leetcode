class Solution:
    def recursive(self, nums, choose, cur, ans):
        if cur==len(nums):
            stk = []
            
            for i, num in enumerate(nums):
                if choose[i]==True:
                    stk.append(num)
            
            stk.sort()
            
            if stk not in ans:
                ans.append(stk)
        
        else:
            choose[cur] = True
            self.recursive(nums, choose, cur+1, ans)
            choose[cur] = False
            self.recursive(nums, choose, cur+1, ans)
            
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        choose = [True]*len(nums)
        self.recursive(nums, choose, 0, ans)
        
        return ans