class Solution:
    def myAtoi(self, str: str) -> int:
        num = ''


        for i in range(0, len(str)):
            if str[i] == ' ' and num =='':
                continue
            elif (str[i] == '+' or str[i] == '-') and num == '':
                num = num + str[i]
            elif str[i].isdigit():
                num = num + str[i]
            else:
                break

        try:
            num = int(num)
        except:
            num = 0

        if num > 2147483647 :
            num = 2147483647
        elif num < -2147483648:
            num = -2147483648

        return num