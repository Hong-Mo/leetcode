class Solution:
    def recursive(self, dic, keys, choose, cur, ans):
        if cur==len(keys):
            stk = [[]]
            
            for i, num in enumerate(keys):
                ins = []
                
                if choose[i]==True:
                    times = dic[num]
                    
                    while stk:
                        sub = stk.pop()
                        
                        for i in range(1, times+1):
                            add = sub[:]
                            
                            for j in range(i):
                                add.append(num)
                            
                            ins.append(add)
                
                stk.extend(ins)
            
            ans.extend(stk)
            
        else:
            choose[cur] = True
            self.recursive(dic, keys, choose, cur+1, ans)
            choose[cur] = False
            self.recursive(dic, keys, choose, cur+1, ans)
            
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        
        for num in nums:
            if num not in dic.keys():
                dic[num] = 1
            
            else:
                dic[num] += 1
        
        choose, ans = [True]*len(dic.keys()), []

        self.recursive(dic, list(dic.keys()), choose, 0, ans)
        
        return ans