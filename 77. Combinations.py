class Solution:
    def choose(self, cur, stk, ans, n, k):
        if len(stk)==k:
            ans.append(stk[:])
        
        elif cur<=n and k-len(stk)<=n-cur+1:
            stk.append(cur)
            self.choose(cur+1, stk, ans, n, k)
            stk.remove(cur)
            self.choose(cur+1, stk, ans, n, k)
            
    def combine(self, n: int, k: int) -> List[List[int]]:
        stk, ans = [], []
        self.choose(1, stk, ans, n, k)
        
        return ans