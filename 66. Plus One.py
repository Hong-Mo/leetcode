class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num = 1
        mul = 1
        
        for i in range(len(digits)-1, -1, -1):
            num = num + (mul*digits[i])
            mul = mul * 10
            
        num = str(num)
        
        
        ans = []
        
        for c in num :
            ans.append(int(c))
            
        return ans