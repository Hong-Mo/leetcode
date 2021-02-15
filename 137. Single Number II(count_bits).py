class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = [0]*32
        
        for num in nums:
            for i in range(31, -1, -1):
                if num%2==1:
                    count[i]+=1
                
                num //= 2
        
        base, ans = 1, 0
        
        for i in range(31, -1, -1):
            if count[i]%3!=0:
                ans += base
            
            base *= 2
        
        if ans>=2**31:
            ans -= 2**32
        
        return ans