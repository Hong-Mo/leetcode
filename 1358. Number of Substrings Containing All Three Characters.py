class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pos = [-1, -1, -1]
        ans = 0
        
        for i, c in enumerate(s):
            pos[ord(c)-97] = i
            ans += (min(pos)+1)
        
        return ans