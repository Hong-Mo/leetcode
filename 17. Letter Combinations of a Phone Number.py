class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', 
               '7':'pqrs', '8':'tuv', '9':'wxyz'}
        ans = ['']
        
        for num in digits:
            ins = []
            
            while ans:
                s, corres = ans.pop(0), dic[num]
                
                for letter in corres:
                    ins.append(s+letter)
            
            ans.extend(ins)
        
        if len(digits)==0:
            del ans[0]
        
        return ans