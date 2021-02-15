class Solution:
    def recursive(self, n, dic):
        ans = 0
    
        for i in range(1, n+1):
            if (i-1) in dic.keys():
                a = dic[i-1]
            
            else:
                a = self.recursive(i-1, dic)
                dic[i-1] = a
            
            if (n-i) in dic.keys():
                b = dic[n-i]
            
            else:
                b = self.recursive(n-i, dic)
                dic[n-i] = b
            
            ans += a*b
            
        return ans
        
    def numTrees(self, n: int) -> int:
        dic = {0:1}
        
        ans = self.recursive(n, dic)
        
        return ans