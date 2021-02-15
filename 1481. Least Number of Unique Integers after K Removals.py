from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr, k: int) -> int:        
        element = []

        counter = Counter(arr)
        counter = dict(counter)
        
        for i in counter.values():
            element.append(i)
        
        element.sort()
        
        while k>0 and k >= element[0]  :
            k -= element[0]
            del element[0]
                   
        return len(element)