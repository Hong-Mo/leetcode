class Solution:
    def maxRepOpt1(self, text: str) -> int:
        ans, l, head = 1, [1]*len(text), [0]*26
        head[ord(text[0])-97] += 1
        
        for i in range(len(text)-1, 0, -1):
            if text[i]==text[i-1]:
                l[i-1] += l[i]
            
            else:
                head[ord(text[i])-97] += 1
        
        for i in range(len(text)):
            cur = l[i]
            if (i-1<0 or l[i-1]<=cur) and (i+1==len(text) or cur>=l[i+1]) and\
               (i+cur+1<len(text) and text[i]==text[i+cur+1]):
                cur += l[i+cur+1]
                
                if head[ord(text[i])-97]>2:
                    cur += 1
            
            elif head[ord(text[i])-97]>1:
                cur += 1
                
            ans = max(ans, cur)

        return ans