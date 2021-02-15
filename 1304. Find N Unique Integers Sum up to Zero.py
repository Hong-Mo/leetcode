class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        num = 500
        
        for i in range(0, n//2):
            ans.extend([num, -num])
            num -= 1
        
        if n%2!=0:
            ans.append(0)
        
        return ans