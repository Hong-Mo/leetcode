class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k==0 or t<0:
            return False
        
        if len(nums)<=k:
            k = len(nums)-1
            scope = nums[:]
        
        else:
            scope = nums[:k+1]
        
        scope.sort()
        
        for i in range(0, k):
            dif = scope[i+1]-scope[i]
                
            if dif<=t:
                return True
        
        start = 0

        for i in range(k+1, len(nums)):
            scope.remove(nums[start])
            j = 0
            
            while j<len(scope) and scope[j]<nums[i]:
                j += 1
            
            scope.insert(j, nums[i])
            
            if j==0:
                dif = scope[j+1]-scope[j]
            
            elif j==len(scope)-1:
                dif = scope[j]-scope[j-1]
            
            else:
                dif = min(scope[j]-scope[j-1], scope[j+1]-scope[j]) 
            
            if dif<=t:
                return True
            
            start += 1
            
        return False