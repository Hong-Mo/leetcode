class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        two_p = 2
        li = [0, 1]
        
        l = pow(2, n)
        
        while len(li) < l :
            top = len(li) - 1
            
            for i in range(top, -1, -1):
                li.append(li[i] + two_p)
            
            two_p *= 2
        
        index = li.index(start)
        side = l-index
        
        ans = []
        ans[:side] = li[index:]
        ans[side:] = li[:index]
        
        return ans