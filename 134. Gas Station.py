class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        dif = []
        ans = -1
        
        for i in range(len(gas)):
            dif.append(gas[i]-cost[i])
        
        if sum(dif)>=0:
            cur = 0
            
            while dif[cur]<0:
                cur += 1
            
            ans, remain = cur, 0
            
            while cur<len(dif):
                if dif[cur]>=0 and remain<0:
                    ans, remain = cur, 0
                
                remain += dif[cur]
                cur += 1
            
        return ans