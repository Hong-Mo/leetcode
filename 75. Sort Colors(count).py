class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0]*3
        
        for color in nums:
            count[color] += 1
        
        start = 0
        
        for color ,quan in enumerate(count):
            nums[start:start+quan] = [color]*quan
            start += quan