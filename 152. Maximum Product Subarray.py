class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pro, cur, first, ans = 1, 0, 0, min(nums)
        
        for num in nums:
            if pro!=0:
                pro *= num
            
            else:
                pro, cur, first = num, 0, 0
                
            if num<0:
                cur += 1
                
                if first==0:
                    first = pro
                    continue
            
            if cur%2==0:
                ans = max(pro, ans)
            
            else:
                ans = max(pro//first, ans)
        
        return ans