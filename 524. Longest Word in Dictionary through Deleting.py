class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        word = {i:w for i, w in enumerate(d)}
        ans, d = '', [list(w) for w in d]
        
        for c in s:
            for i in range(len(d)):
                if d[i] and d[i][0]==c:
                    d[i].pop(0)
                    
                    if not d[i] and (len(word[i])>len(ans) or\
                       (len(word[i])==len(ans) and word[i]<ans)):
                        ans = word[i]
        
        return ans