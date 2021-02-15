class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        order = []
        num, count = 1, n
        
        while count>0:
            
            while num<=n:
                order.append(num)
                num *= 10
                count -= 1
            
            num //= 10
            
            for i in range(0, 10):
                num += 1
                
                if num>=n or num%10==0  or count==0 :
                    break
                
                order.append(num)
                count -= 1
            
            if num==n and num%10!=0:
                order.append(num)
                count -= 1
                num //= 10
                num += 1
            
            while num%10==0:
                num //= 10
    
        return order