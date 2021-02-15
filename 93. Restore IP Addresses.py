class Solution:
    def recursive(self, s, cur, dot, store, ans):
        if dot==3:
            if cur!=len(s) and ((int(s[cur:])>0 and int(s[cur:])<256 and s[cur]!='0') or s[cur:]=='0') :
                store += s[cur:]
                ans.append(store)
        
        else:
            start = 1

            while (cur+start)<=len(s) and int(s[cur:cur+start])<256:
                send = store + s[cur:cur+start] + '.'
                self.recursive(s, cur+start, dot+1, send, ans)

                if s[cur:cur+start] == '0':
                    break

                start += 1
            
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.recursive(s, 0, 0, '', ans)
        
        return ans