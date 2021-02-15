class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0:-1}
        cur = 0

        for i, num in enumerate(nums):
            if k!=0:
                cur = (cur+num)%k
            
            else:
                cur += num
            
            if cur in dic.keys():
                if i-1>dic[cur]:
                    return True
            
            else:
                dic[cur] = i
        
        return False