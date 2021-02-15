class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        num = 0

        while i < len(s):
            if s [i] == 'M':
                num = num + 1000

            elif s[i] == 'D':
                num = num + 500

            elif s[i] == 'C':
                try:
                    if s[i+1] == 'M':
                        num = num + 900
                        i = i + 1

                    elif s[i+1] == 'D':
                        num = num + 400
                        i = i + 1

                    else:
                        num = num + 100

                except:
                    num = num + 100

            elif s[i] == 'L':
                num = num + 50

            elif s[i] == 'X':
                try:
                    if s[i+1] == 'C':
                        num = num + 90
                        i = i + 1

                    elif s[i+1] == 'L':
                        num = num + 40
                        i = i + 1

                    else:
                        num = num + 10

                except:
                    num = num + 10

            elif s[i] == 'V':
                num = num + 5

            elif s[i] == 'I':
                try:
                    if s[i+1] == 'X':
                        num = num + 9
                        i = i + 1

                    elif s[i+1] == 'V':
                        num = num + 4
                        i = i + 1

                    else:
                        num = num + 1

                except:
                    num = num + 1

            i = i + 1

        return num