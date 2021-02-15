class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort()
        start = 0
        
        while start<len(A) and A[start]<0:
            start += 1
        
        B = A[:start]
        B.reverse()
        A[:start]=B
        
        queue = []
        l = len(A)
        
        for num in A:
            check = num/2
            
            if len(queue)!=0 and queue[0] == check:
                del queue[0]
            
            else:
                queue.append(num)
            
            if len(queue)>l/2:
                return False
        
        if queue:
            return False
        
        return True