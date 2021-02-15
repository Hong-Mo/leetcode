class Solution:
    def cal_trap(self, interval):
        if not interval:
            return 0
        
        bound = max(interval)
        bound_i = interval.index(bound)
        bar = sum(interval[bound_i+1:])
            
        available = (len(interval)-bound_i-1)*bound-bar
        
        return available + self.cal_trap(interval[:bound_i])
    
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        max_i = height.index(max(height))
        second = height[max_i+1:]
        second.reverse()
        
        return self.cal_trap(height[:max_i]) + self.cal_trap(second)