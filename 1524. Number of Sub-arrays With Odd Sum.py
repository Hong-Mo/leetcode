class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        count = [1, 0] # 0:even, 1:odd
        ans, cur = 0, 0
        
        for num in arr:
            cur = (cur+num)%2
            ans += count[(cur+1)%2]
            count[cur] += 1
        
        return ans%(pow(10, 9) + 7)