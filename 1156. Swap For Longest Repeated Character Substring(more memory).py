class Solution:
    def maxRepOpt1(self, text: str) -> int:
        cur, ans, head = 0, 1, [[] for i in range(26)]
        
        while cur<len(text):
            start = cur
            
            while cur<len(text)-1 and text[cur]==text[cur+1]:
                cur += 1
        
            head[ord(text[cur])-97].append((start, cur-start+1))
            ans, cur = max(ans, cur-start+1), cur+1
        
        for l_seq in head:
            for i in range(len(l_seq)-1):
                front, behind = l_seq[i], l_seq[i+1]
                l = front[1]+1
                
                if sum(front)+1==behind[0]:
                    l += behind[1]
                
                    if len(l_seq)<3:
                        l -= 1
                
                ans = max(ans, l)
        
            if len(l_seq)>1:
                ans = max(ans, l_seq[-1][1]+1)
        
        return ans