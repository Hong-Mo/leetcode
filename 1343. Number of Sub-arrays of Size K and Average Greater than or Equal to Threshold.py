class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        std = k*threshold
        head, ans, tail = 0, 0, k-1
        cur = sum(arr[:tail])+arr[head-1]

        while tail<len(arr):
            cur -= arr[head-1]
            cur += arr[tail]

            if cur>=std:
                ans += 1
            
            head += 1
            tail += 1
            
        return ans