class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        li = set(nums)
        ans = sum(li)*2-sum(nums)
        
        return ans