class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        remain = ans = 0
        count = [0]*K
        count[0] = 1
        
        for num in A:
            remain = (remain+num)%K
            ans += count[remain]
            count[remain] += 1
        
        return ans