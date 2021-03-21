class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        
        for i in range(len(arr)):
            left, right = i/2, (len(arr)-i-1)/2
            even = (math.floor(left)+1)*(math.floor(right)+1)
            odd = math.ceil(left)*math.ceil(right)
            ans += (even+odd)*arr[i]
        
        return ans