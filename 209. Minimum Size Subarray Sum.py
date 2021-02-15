class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l, r = 0, -1
        acc, ans = 0, len(nums)+1
        
        while r<len(nums)-1:
            while acc<s and r<len(nums)-1:
                r += 1
                acc += nums[r]
            
            while acc>=s:
                acc, ans = acc-nums[l], min(ans, r-l+1)
                l += 1
        
        if ans==len(nums)+1:
            return 0
        
        return ans