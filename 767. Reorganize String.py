class Solution:
    def reorganizeString(self, S: str) -> str:
        ans, count = '', [0]*26
        
        for c in S:
            count[ord(c)-97] += 1
        
        pre = count.index(max(count))
        ans, count[pre]= ans+chr(pre+97), count[pre]-1

        for i in range(len(S)-1):
            s, count[pre] = count[pre], 0
            cur = count.index(max(count))
            
            if count[cur]==0:
                return ''
            
            ans, count[cur], count[pre] = ans+chr(cur+97), count[cur]-1, s
            pre = cur

        return ans