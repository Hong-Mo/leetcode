class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
        odd = []
        even = []
        
        for i in range(0, len(A)):
            if A[i]%2 != 0:
                odd.append(A[i])
            
            else:
                even.append(A[i])
        
        
        for i in range(0, len(A)):
            if i % 2 != 0:
                A[i] = odd.pop()
                
            else:
                A[i] = even.pop()
        
        return A