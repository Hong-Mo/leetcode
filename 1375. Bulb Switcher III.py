class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        check = current = 0
        count = 1
        
        for i in range(1, len(light)):
            current += light[i-1]
            check += i
            
            if current == check:
                count += 1
            
        return count