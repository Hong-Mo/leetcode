class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = {}
        
        for n in nums:
            if n in count.keys():
                count[n] += 1
            
            else:
                count[n] = 1
        
        pre = cur = 0
        value = sorted(count.keys())
        
        for i in range(0, len(value)):
            store = cur
            plus = value[i]*count[value[i]]
            
            if value[i]-1 == value[i-1]:
                cur = max(pre+plus, cur)
            
            else:
                cur += plus
            
            pre = store
            
        return cur