class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        queue = []
        
        for num in nums: 
            ins = []
            judge =  0

            while queue:
                add = [num]
                j = len(queue[0])-1
                
                while j>=0 and queue[0][j]>num:
                    j -= 1
                
                ins.append(queue[0])
                
                if j>=0 :
                    judge = 1
                    
                    if queue[0][j]!=num:
                        add[:0] = queue[0][:j+1]
                        ins.append(add)
                    
                        if j == len(queue[0])-1:
                            del ins[-2]
                
                del queue[0]

            if judge == 0:
                ins.append([num])
            
            queue.extend(ins)
        
        ans = 0
        
        if queue:    
            ans = max([len(sub) for sub in queue])
        
        return ans