class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        base = 1
        
        while n>0:
            ins = []
            
            for i in range(len(ans)-1, -1, -1):
                ins.append(ans[i]+base)
            
            ans.extend(ins)
            n, base = n-1, base*2
        
        return ans