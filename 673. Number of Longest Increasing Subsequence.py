class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        stk = []
        max_len = ans = 0
        
        for i, num, in enumerate(nums):
            data = [0, 1]#max, count
            
            for j in range(0, i):
                cur = stk[j]
                
                if num>nums[j]:
                    if cur[0]>data[0]:
                        data[0] = cur[0]
                        data[1] = cur[1]
                
                    elif cur[0]==data[0]:
                        data[1] += cur[1]
                
            data[0] += 1
            max_len = max(data[0], max_len)
            stk.append(data)
            
        for d in stk:
            if d[0]==max_len:
                ans += d[1]
        
        return ans