class Solution:
    def reverse(self, x: int) -> int:
        neg = 0
        if x < 0 :
            neg = 1
            x = 0 - x
        digit = []

        while x > 0:
            digit.append(x%10)
            x = x // 10

        digit_str = ''

        if neg == 1 :
            digit_str  = digit_str + '-'

        for i in range(0, len(digit)):
            digit_str = digit_str + str(digit[i])

        if digit_str == '' or int(digit_str)>=2147483648 or int(digit_str)<-2147483648:
            digit_str = '0'


        return int(digit_str)