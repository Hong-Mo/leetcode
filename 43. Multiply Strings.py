class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mul = 1
        sum1 = 0
        sum2 = 0

        for i in range(len(num1)-1, -1, -1):
            sum1 = sum1 +((ord(num1[i])-48)*mul)
            mul = mul * 10

        mul = 1

        for i in range(len(num2)-1, -1, -1):
            sum2 = sum2 +((ord(num2[i])-48)*mul)
            mul = mul * 10

        return str(sum1*sum2)