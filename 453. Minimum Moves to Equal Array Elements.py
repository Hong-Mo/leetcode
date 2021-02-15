class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        nums = [(num-min_num) for num in nums]
        ans = sum(nums)
        
        return ans
