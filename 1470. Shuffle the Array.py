class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        
        for i in range(0, n):
            ans.extend([nums[i], nums[i+n]])
        
        return ans