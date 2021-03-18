class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        cur = ans = 0
        
        while cur<len(A):
            acc = 0
            
            while cur<len(A) and (A[cur]<L or A[cur]>R):
                if A[cur]<L:
                    acc += 1
                
                else:
                    acc = 0
                    
                cur += 1

            while cur<len(A) and A[cur]<=R:
                less = 0
                
                while cur<len(A) and A[cur]>=L and A[cur]<=R:
                    acc += 1
                    ans, cur = ans+acc, cur+1
                
                while cur<len(A) and A[cur]<L:
                    ans, cur, less = ans+acc, cur+1, less+1
                
                acc += less

        return ans