class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        
        dif, last, cur, ans = nums[1]-nums[0], 0, 1, 0
        
        while cur<len(nums)-1:
            while cur<len(nums)-1 and nums[cur+1]-nums[cur]==dif:
                cur += 1

            l = (cur-last)+1
            
            for i in range(3, l+1):
                ans += (l-(i-1))
            
            last, cur = cur, cur+1
            
            if cur<len(nums)-1:
                dif = nums[cur]-nums[cur-1]
        
        return ans