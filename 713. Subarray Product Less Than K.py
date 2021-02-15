class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        queue = []
        mul, ans = 1, 0
        
        for num in nums:
            while queue and mul*num>=k:
                mul //= queue[0]
                del queue[0]
                
            if mul*num<k:
                mul *= num
                queue.append(num)
                ans += len(queue)

        return ans