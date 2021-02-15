class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        s = {''}
        
        for c in tiles:
            per = set()
            
            for d in s:
                
                for i in range(0, len(d)+1):
                    per.add(d[:i]+c+d[i:])
            
            s |= per
        
        return len(s)-1