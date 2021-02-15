class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        pos = 0
        
        while pos<len(intervals):
            cur = intervals[pos]
            
            if (cur[0]>=newInterval[0] and cur[0]<=newInterval[1])\
                or (cur[1]>=newInterval[0] and cur[1]<=newInterval[1]):
                newInterval = [min(cur[0], newInterval[0]), max(cur[1], newInterval[1])]
                del intervals[pos]
                pos -= 1
            
            elif cur[0]>newInterval[1]:
                intervals.insert(pos, newInterval)
                return intervals
            
            elif cur[0]<=newInterval[0] and cur[1]>=newInterval[1]:
                return intervals
            
            pos += 1
        
        intervals.append(newInterval)
        
        return intervals