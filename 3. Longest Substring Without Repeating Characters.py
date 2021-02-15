class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tail = 0
        ans = 0
        l = len(s)
        queue = []
        
        while tail < l:
            
            if s[tail] in queue :
                index = queue.index(s[tail])
                del queue[:index+1]

            queue.append(s[tail])
            count = len(queue)
                
            if count > ans :
                ans = count
            
            tail += 1
        
        return ans 