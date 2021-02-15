class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        index = []

        index = sorted(range(0, len(nums)), key=lambda i: nums[i], reverse =True)


        for i in range(0, len(index)):
            if i == 0:
                nums[index[i]] = 'Gold Medal'
            elif i == 1:
                nums[index[i]] = 'Silver Medal'
            elif i == 2:
                nums[index[i]] = 'Bronze Medal'
            else:
                nums[index[i]] = str(i+1)

        return nums