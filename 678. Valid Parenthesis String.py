class Solution:
    def checkValidString(self, s: str) -> bool:
        top = -1
        stk = []

        for c in s :

            if c != ')':
                stk.append(c)
                top += 1

            else:

                if len(stk) == 0:
                    return False

                if '(' in stk:
                    for i in range(top, -1, -1):
                        if stk[i] == '(':
                            del stk[i]
                            top -= 1
                            break
                else:
                    stk.pop()
                    top -= 1

        while '(' in stk :
            if stk[-1] == '(':
                return False

            else:
                for i in range(top, -1, -1):
                        if stk[i] == '(':
                            del stk[i]
                            del stk[-1]
                            top -= 2
                            break

        return True