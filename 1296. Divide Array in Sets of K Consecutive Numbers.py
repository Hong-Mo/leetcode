class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        dic = {}
        
        for num in nums:
            if num not in dic.keys():
                dic[num] = 1
            
            else:
                dic[num] += 1
        
        nums = sorted(dic.keys())
        
        while nums:
            cur = nums[0]
            
            for i in range(k):
                try:
                    dic[cur] -= 1
                    
                    if dic[cur]==0:
                        del dic[cur]
                        nums.remove(cur)
                
                except:
                    return False
                
                cur += 1

        return True