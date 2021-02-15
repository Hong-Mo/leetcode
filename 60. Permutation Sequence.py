class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        per, cur, stairs, remain = [], 0, 1, k-1
        
        for i in range(1, n+1):
            stairs *= i
            per.append(str(i))
        
        stairs //= n
        
        while remain>0:
            quot, remain = divmod(remain, stairs)
            per.insert(cur, per.pop(cur+quot))

            stairs //= (n-1)
            cur, n = cur+1, n-1
        
        return ''.join(per)