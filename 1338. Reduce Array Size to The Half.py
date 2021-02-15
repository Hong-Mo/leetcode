class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        collect, counter = {}, {}
        
        for num in arr:
            if num not in collect.keys():
                collect[num] = 1
            
            else:
                collect[num] += 1
        
        for v in collect.values():
            if v not in counter.keys():
                counter[v] = 1
            
            else:
                counter[v] += 1
        
        l = len(arr)
        half_len = l/2
        ans = 0
        max_len= max(counter.keys())
        nums = counter[max_len]
        
        while l>half_len:
            if nums==0:
                del counter[max_len]
                max_len= max(counter.keys())
                nums = counter[max_len]
                
            l -= max_len
            nums -= 1
            ans += 1
        
        return ans