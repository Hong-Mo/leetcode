class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        dic = {}
        
        for num in nums:
            if num in dic.keys():
                dic[num] += 1
            
            else:
                dic[num] = 1
        
        side = sorted(dic.keys())
        
        