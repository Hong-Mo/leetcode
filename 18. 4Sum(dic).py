class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        dic = {}
        ans = set()
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                plus = nums[i]+nums[j]
                
                if plus in dic.keys():
                    dic[plus].append([(i ,j), (nums[i], nums[j])])
                
                else:
                    dic[plus] = [[(i ,j), (nums[i], nums[j])]]
        
        search = sorted(dic.keys())
        left, right = 0, len(search)-1
        
        while left<=right:
            plus = search[left]+search[right]
            
            if plus<target:
                left += 1
            
            elif plus>target:
                right -= 1
            
            else:
                for i_l, v_l in dic[search[left]]:
                    for i_r, v_r in dic[search[right]]:
                        if i_l[0] not in i_r and i_l[1] not in i_r:
                            ins = sorted([v_l[0], v_l[1], v_r[0], v_r[1]])
                            ans.add(tuple(ins))
                
                left, right = left+1, right-1
        
        ans = [list(seq) for seq in ans]
        
        return ans