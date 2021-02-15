class Solution:
    def originalDigits(self, s: str) -> str:
        dic = {1:{'z':'zero', 'w':'two', 'u':'four', 'x':'six', 'g':'eight'}, 
               2:{'o':'one', 't':'three', 'f':'five', 's':'seven'}, 
               3:{'i':'nine'}}
        word_int = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 
                    'six':6, 'seven':7, 'eight':8, 'nine':9}
        count = {}
        
        for c in s:
            if c in count.keys():
                count[c] += 1
            
            else:
                count[c] = 1
        
        num = [0]*10
        
        for i in range(1,4):
            find = dic[i]
            
            for k, v in find.items():
                if k in count.keys():
                    times = count[k]

                    for c in v:
                        count[c] -= times
                    
                        if count[c]==0:
                            del count[c]
                        
                    digit = word_int[v]
                    num[digit] += times
        
        ans = ''
        
        for i in range(0, 10):
            
            for j in range(0, num[i]):
                ans += str(i)
        
        return ans