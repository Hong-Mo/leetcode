class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        max_len = 0
        dic = {}
        
        for i, num in enumerate(arr):
            data, minus = 0, (num-difference)
            
            if minus in dic.keys():
                data = dic[minus]
            
            data += 1
            dic[num] = data
            max_len = max(data, max_len)
        
        return max_len