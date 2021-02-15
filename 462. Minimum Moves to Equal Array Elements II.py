class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        std, ans = nums[l//2], 0
        
        for num in nums:
            ans += abs(std-num)
        
        return ans