class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        dic = {0:[[]], target:[]}
        candidates.sort()
        
        for num in candidates:
            ins = {}
            limit = target-num
            
            for k, val in dic.items():
                check = k+num
                
                if check<=limit or check==target:
                    ins[check] = []
                    
                    for arr in val:
                        add = arr[:]
                        add.append(num)
                        ins[check].append(add)

            for i, v in ins.items():
                if i not in dic.keys():
                    dic[i] = []
                
                dic[i].extend(v)

        ans = set([tuple(arr) for arr in dic[target]])
        ans = [list(arr) for arr in ans]
            
        return ans