class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        
        while l<r-1:
            m = (l+r)//2
            s = 0
            
            for num in nums:
                s += num//m
                
                if num%m!=0:
                    s += 1
                    
            if s>threshold:
                l = m
            
            else:
                r = m                 
        
        s = 0

        for num in nums:
            s += num//l

            if num%l!=0:
                s += 1

        if s<=threshold:
            return l

        return r