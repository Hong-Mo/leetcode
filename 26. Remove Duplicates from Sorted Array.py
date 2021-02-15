class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l = []
        i = 0

        while i <len(nums):
            try:
                if nums[i] not in l :
                    l.append(nums[i])
                    i = i + 1
                else:
                    del nums[i]
            except :
                break



        return len(nums)
