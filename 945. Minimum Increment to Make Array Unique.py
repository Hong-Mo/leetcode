class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        ans = 0
        A.sort()

        for cur in range(1, len(A)):
            dif = A[cur-1]-A[cur]
            
            if dif>=0:
                ans, A[cur] = ans+(dif+1), A[cur-1]+1
        
        return ans