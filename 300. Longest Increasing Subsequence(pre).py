class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stk = []
        max_len = 0
        
        for i, num in enumerate(nums):
            data = 0
            
            for j in range(0, i):
                if num>nums[j] and stk[j]>data:
                    data = stk[j]
            
            data += 1
            max_len = max(data, max_len)
            stk.append(data)
        
        return max_len