class Solution:
    def findNthDigit(self, n: int) -> int:
        ini, ten, base = 9, 10, 1
        
        while n>(base*ini):
            n -= (base*ini)
            base += 1
            ini *= ten
        
        ini //= 9
        num, remain = divmod(n, base)
        num += (ini-1)
        
        if remain != 0:
            num += 1
        
        else:
            remain = base
            
        num = str(num)
        ans = num[remain-1]
        
        return int(ans)