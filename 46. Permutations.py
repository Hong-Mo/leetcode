class Solution:
    def per_recursive (self, nums, j, li):

        if j == len(nums):
            li.append(nums[:])

        for i in range(j, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            Solution.per_recursive(self, nums, j+1, li)
            nums[i], nums[j] = nums[j], nums[i]
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        li = []
        self.per_recursive(nums, 0, li)
        
        return li