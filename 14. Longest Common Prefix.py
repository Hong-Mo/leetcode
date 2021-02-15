class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ''
        commom = 0

        while len(strs)!=0 :
            judge = 1
            for i in range(0, len(strs)):
                try:
                    if strs[0][commom] != strs[i][commom]:
                        judge = 0
                        break
                except:
                    judge = 0
                    break

            if judge == 1 :
                pre = pre + strs[0][commom]
            else:
                break

            commom = commom + 1

        return pre