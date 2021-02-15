class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stk, ans = [], [0]*len(T)
        
        for cur, num in enumerate(T):
            while stk and num>stk[-1][1]:
                p, p_temp = stk.pop()
                ans[p] = cur-p
            
            stk.append((cur, num))
        
        return ans