class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk, ans = [], [-1]*len(nums)
        
        for i in range(2):
            for cur, cur_num in enumerate(nums):
                while stk and cur_num>stk[-1][1]:
                    past, past_num = stk.pop()
                    ans[past] = cur_num
            
                stk.append((cur, cur_num))
        
        return ans