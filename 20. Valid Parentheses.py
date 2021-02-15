class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
    
        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stk.append(s[i])

            elif s[i] == ')':
                try:
                    if stk.pop()!='(':
                        return False
                except :
                     return False

            elif s[i] == ']':
                try:
                    if stk.pop()!='[':
                        return False
                except :
                     return False

            elif s[i] == '}':
                try:
                    if stk.pop()!='{':
                        return False
                except :
                     return False
                 
        if len(stk)!=0:
            return False


        return True