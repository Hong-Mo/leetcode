class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        pre, ans = -1, 0
        count = [0, 0]
        
        for num in nums:
            if num==1:
                count[1] += 1
            
            elif pre!=0:
                ans = max(ans, sum(count))
                count[0], count[1] = count[1], 0
            
            else:
                count[0] = 0
            
            pre = num
        
        ans = max(ans, sum(count))
        
        if 0 not in nums:
            ans -= 1

        return ans