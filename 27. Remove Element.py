class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
    
        while i < len(nums):
            try:
                if val == nums[i]:
                    del nums[i]

                else:
                    i = i + 1

            except :
                break

        return len(nums)