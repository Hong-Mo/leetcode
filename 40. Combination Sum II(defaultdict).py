class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        dic = collections.defaultdict(list)
        dic[0].append([])
        candidates.sort()
        
        for num in candidates:
            ins = collections.defaultdict(list)
            limit = target-num
            
            for k, val in dic.items():
                check = k+num
                
                if check<=limit or check==target:
                    for arr in val:
                        add = arr[:]
                        add.append(num)
                        ins[check].append(add)
                
            for i, v in ins.items():
                dic[i].extend(v)
        
        ans = set([tuple(arr) for arr in dic[target]])
        ans = [list(arr) for arr in ans]
            
        return ans