class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg, quo = 0, 0
        
        if dividend^divisor<0:
            neg = 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)<<32
        
        for i in range(32):
            quo <<= 1
            divisor >>= 1
            
            if dividend>=0:
                dividend -= divisor
            
            else:
                dividend += divisor
            
            if dividend>=0:
                quo += 1
        
        if neg==1:
            quo = -quo
        
        if quo<-pow(2, 31) or quo>pow(2, 31)-1:
            quo = pow(2, 31)-1
        
        return quo