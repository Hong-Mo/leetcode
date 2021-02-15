class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        store = [0]
        cur = 0
        
        for i in range(1, len(nums)+1):
            if k!=0:
                cur = (cur+nums[i-1])%k
            
            else:
                cur += nums[i-1]
            
            if (cur in store) and (i-1>store.index(cur)):
                return True
            
            store.append(cur)
        
        return False