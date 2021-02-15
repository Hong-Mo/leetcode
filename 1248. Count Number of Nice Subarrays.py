class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [n%2 for n in nums]
        odd = ans = 0
        
        com_num, left, right = [[0, 0] for i in range(len(nums))], 0, len(nums)-1
        l_o, r_o = -1, len(nums)
        
        while left<len(nums):
            if nums[left]==1:
                com_num[left][0], l_o = left-l_o, left
            
            if nums[right]==1:
                com_num[right][1], r_o = r_o-right, right
            
            left, right = left+1, right-1
        
        left = right = 0
        
        while right<len(nums):
            while right<len(nums) and odd!=k:
                odd, right= odd+nums[right], right+1
            
            while odd==k and nums[left]!=1:
                left += 1

            ans, left, odd = ans+com_num[left][0]*com_num[right-1][1], left+1, odd-1
            
        return ans