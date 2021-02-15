class Solution:
    def candy(self, ratings: List[int]) -> int:
        least = ['x']*len(ratings)
        ratings.append(ratings[-1])
        ratings.insert(0, ratings[0])
        
        l, r ,step = 1, len(ratings)-2, 1
        
        for i in range(2):
            for cur in range(l, r+step, step):
                if ratings[cur]<=ratings[cur-1] and ratings[cur]<=ratings[cur+1]:
                    least[cur-1] = 1
                
                elif ratings[cur]<=ratings[cur+1] and ratings[cur]>ratings[cur-1]:
                    if least[cur-2]!='x':
                        least[cur-1] = least[cur-2]+1
                
                elif ratings[cur]<=ratings[cur-1] and ratings[cur]>ratings[cur+1]:
                    if least[cur]!='x':
                        least[cur-1] = least[cur]+1
                
                elif least[cur]!='x' and least[cur-2]!='x':
                    least[cur-1] = max(least[cur-2], least[cur])+1
            
            l, r, step = r, l, -step
            
        return sum(least)