class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = [0]*len(arr)
        
        for i in range(len(arr)):
            cur, count[i] = arr[i]-1, count[i]+i+1
            
            if cur<len(count):
                count[cur] -= 1
        
        for i in range(len(count)-1, -1, -1):
            if count[i]==0:
                return i+1
        
        return -1