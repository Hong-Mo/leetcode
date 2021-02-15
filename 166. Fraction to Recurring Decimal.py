class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        quotient, remainder = divmod(abs(numerator), abs(denominator))
        ans = ''
        
        if numerator*denominator<0:
            ans += '-'
            
        ans += str(quotient)
        
        if remainder != 0:
            ans += '.'
        
        result = ''
        stk = []
        
        while remainder not in stk:
            stk.append(remainder)
            quotient, remainder = divmod(remainder*10, abs(denominator))
            result += str(quotient)
        
        if remainder != 0:
            repeat = stk.index(remainder)
            result = result[:repeat]+'('+result[repeat:]+')'
        
        else:
            result = result[:-1]
        
        ans += result
        
        return ans