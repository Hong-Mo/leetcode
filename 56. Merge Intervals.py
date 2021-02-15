class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr = [] 
        
        while intervals :
            li = intervals[0]
            judge = 0
            count = 0
            
            while count < len(arr):
                
                r = arr[count]
                
                if (li[0] <= r[0]) and (r[0] <= li[1]):
                    intervals[0] = li = [li[0], max(r[1], li[1])]
                    arr.remove(r)
                    continue
            
                elif (r[0] <= li[0]) and (li[0] <= r[1]):
                    intervals[0] = li = [r[0], max(r[1], li[1])]
                    arr.remove(r)
                    continue
                
                count += 1
            
            
            arr.append(intervals[0])
            del intervals[0]
        
        return arr