class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        li = text.split(' ')
        ans = []
        
        for i in range(2, len(li)):
            if li[i-2]==first and li[i-1]==second:
                ans.append(li[i])
        
        return ans