class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A, ans, left = sorted(A), [False]*len(A), []
        B = [(i, num) for i, num in enumerate(B)]
        B = sorted(B, key=lambda x:x[1])
        
        while A:
            num = A.pop(0)
            i, cmp = B[0]
            
            if num>cmp:
                ans[i] = num
                del B[0]
            
            else:
                left.append(num)
            
        for i in range(len(ans)):
            if ans[i] == False:
                ans[i] = left.pop()                
        
        return ans