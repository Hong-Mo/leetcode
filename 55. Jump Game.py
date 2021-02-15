class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = []
        
        for i, num in enumerate(nums):
            jump.append(i+num)
        
        pre, start, end = -1, 0, len(nums)-1
        scope = jump[start]
        
        while pre!=start:
            pre = start
            
            if scope>=end:
                return True
            
            for i in range(start+1, scope+1):
                if jump[i]>scope:
                    scope = jump[i]
                    start = i
        
        return False