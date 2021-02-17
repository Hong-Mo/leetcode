class Solution:
    def numSplits(self, s: str) -> int:
        left = right = ans = 0
        l_count, r_count = {}, {}
        
        for c in s:
            if c not in r_count:
                r_count[c] = 1
            
            else:
                r_count[c] += 1
        
        for c in s:
            if c not in l_count:
                l_count[c] = 1
            
            else:
                l_count[c] += 1
            
            r_count[c] -= 1
            
            if r_count[c]==0:
                del r_count[c]
            
            if len(l_count)==len(r_count):
                ans += 1
            
        return ans