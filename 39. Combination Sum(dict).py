class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dic = {0:[[]], target:[]}
        candidates.sort()
        
        for num in candidates:
            ins = {}
            limit = target-num
            
            for k, val in dic.items():
                check = k+num
                stk = [v[:] for v in val]
                
                while check<limit:
                    
                    for arr in stk:
                        arr.append(num)
                        
                        if check in ins.keys():
                            ins[check].append(arr[:])
                        
                        else:
                            ins[check] = [arr[:]]
                    
                    check += num
                
                if (target-k)%num==0 and k!=target:
                    for arr in val:
                        add = arr[:]
                        
                        for i in range((target-k)//num):
                            add.append(num)
                        
                        dic[target].append(add)
                
            for i, v in ins.items():
                if i in dic.keys():
                    dic[i].extend(v)

                else:
                    dic[i] = v
            
        return dic[target]