class Solution:
    def simplifyPath(self, path: str) -> str:
        dir_name = []
        cur = 0
        
        while cur<len(path):
            while cur<len(path) and path[cur]=='/':
                cur += 1
            
            store = ''
            
            while cur<len(path) and path[cur]!='/':
                store += path[cur]
                cur += 1
            
            if store:
                dir_name.append(store)
        
        cur = 0
        
        while cur<len(dir_name):
            if dir_name[cur] == '..':
                if cur!=0:
                    del dir_name[cur]
                    del dir_name[cur-1]
                    cur -= 2
                
                else:
                    del dir_name[cur]
                    cur -= 1
            
            elif dir_name[cur] == '.':
                del dir_name[cur]
                cur -= 1
            
            cur += 1
        
        ans = ''
        
        for name in dir_name:
            ans += ('/'+name)
            
        if not ans:
            ans += '/'
        
        return ans