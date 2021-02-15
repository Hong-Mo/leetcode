class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans, stk = 0, []
        
        for num in heights:
            count = 0
            
            while stk and stk[-1][0]>=num:
                bound, quan = stk.pop()
                count += quan
                ans = max(ans, bound*(count))
            
            stk.append((num, count+1))

        count = 0
        
        while stk:
            bound, quan = stk.pop()
            count += quan
            ans = max(ans, bound*count)
        
        return ans