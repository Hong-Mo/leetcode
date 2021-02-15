class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dic = collections.defaultdict(list)
        dic[0].append([])
        candidates.sort()
        
        for num in candidates:
            ins = collections.defaultdict(list)
            limit = target-num
            
            for k, val in dic.items():
                check = k+num
                stk = [v[:] for v in val]
                
                while check<limit:
                    
                    for arr in stk:
                        arr.append(num)
                        ins[check].append(arr[:])
                        
                    check += num
                
                if (target-k)%num==0 and k!=target:
                    for arr in val:
                        add = arr[:]
                        
                        for i in range((target-k)//num):
                            add.append(num)
                        
                        ins[target].append(add)
                
            for i, v in ins.items():
                dic[i].extend(v)
            
        return dic[target]