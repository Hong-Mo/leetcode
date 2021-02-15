class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''

        while(num > 0):
            if num >= 1000 :
                frequency = num//1000
                for i in range(0, frequency):
                    roman = roman + 'M'

                num = num - (frequency*1000)

            elif num >= 500:
                frequency = num//100
                if frequency == 9 :
                    roman = roman + 'CM'
                    num = num - 900
                else:
                    roman = roman + 'D'
                    num = num - 500


            elif num >= 100 :
                frequency = num//100
                if frequency == 4 :
                    roman = roman + 'CD'
                else:
                    for i in range(0, frequency):
                        roman = roman + 'C'

                num = num - (frequency*100)

            elif num >= 50:
                frequency = num//10
                if frequency == 9 :
                    roman = roman + 'XC'
                    num = num - 90
                else:
                    roman = roman + 'L'
                    num = num - 50


            elif num >=10:
                frequency = num//10
                if frequency == 4 :
                    roman = roman + 'XL'
                else:
                    for i in range(0, frequency):
                        roman = roman + 'X'

                num = num - (frequency*10)

            elif num >= 5:
                if num == 9 :
                    roman = roman + 'IX'
                    num = num - 9
                else:
                    roman = roman + 'V'
                    num = num - 5
            else:
                if num == 4:
                    roman = roman + 'IV'
                else:
                    for i in range(0, num):
                         roman = roman + 'I'

                num = 0

        return roman
