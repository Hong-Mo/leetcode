class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        stk = []
        ans = 0
        
        for i, num in enumerate(A):
            if not stk or A[stk[-1]]>num:
                stk.append(i)
        
        for i in range(len(A)-1, -1, -1):
            while stk and A[stk[-1]]<=A[i]:
                ans = max(i-stk.pop(), ans)
        
        return ans