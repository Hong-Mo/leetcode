class Solution:
    def choose(self, arr, cur, store, ans):
        if cur==len(arr):
            ans.append(store[26])
        
        else:
            judge = 1
            stk = []
            
            for c in arr[cur]:
                letter = ord(c)-97
                
                if store[letter]==1:
                    while stk:
                        store[stk.pop()] -= 1
                    
                    judge = 0
                    break
                
                else:
                    store[letter] += 1
                    stk.append(letter)
            
            if judge==1:
                store[26] += len(arr[cur])
                
                self.choose(arr, cur+1, store, ans)
            
                for c in arr[cur]:
                    store[ord(c)-97] = 0
                
                store[26] -= len(arr[cur])
                
                self.choose(arr, cur+1, store, ans)
            
            else:
                self.choose(arr, cur+1, store, ans)
                
    def maxLength(self, arr: List[str]) -> int:
        store, ans = [0]*27, []
        self.choose(arr, 0, store, ans)
        
        return max(ans)