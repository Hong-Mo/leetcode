class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        
        start = 0
        
        while A[start]<0 and K>0 :
            A[start] = -A[start]
            K -= 1
            start += 1
        
        A.sort()
        
        if K % 2 !=0:
            A[0] = - A[0]
                    
        
        return sum(A)