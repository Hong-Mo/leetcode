class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = 'balon'
        count = [0]*5
        
        for c in text:
            if c in word:
                count[word.index(c)] += 1
        
        count[2] //= 2
        count[3] //= 2
        
        return min(count)