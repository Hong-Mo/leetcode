class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        queue = [s]
        ans = 0
        
        while queue:
            judge, seg = 1, queue.pop(0)
            
            for c in set(seg):
                if seg.count(c)<k:
                    queue.extend(seg.split(c))
                    judge = 0
                    break
            
            if judge==1:
                ans = max(ans, len(seg))
            
        return ans