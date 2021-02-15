class Solution:
    def findMin(self, nums: List[int]) -> int:
        stk, ans = [nums], []
        
        while stk:
            cur = stk.pop()
            l ,r = 0, len(cur)-1
            
            while l<r:
                mid = (l+r)//2
                
                if cur[mid]<cur[r]:
                    r = mid
                
                elif cur[mid]>cur[r]:
                    l = mid+1
                
                else:
                    stk.append(cur[l:mid])
                    stk.append(cur[mid+1:r+1])
                    break

            if l==r and cur:
                ans.append(cur[l])

        return min(ans)