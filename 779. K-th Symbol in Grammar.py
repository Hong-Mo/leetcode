class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        count = bin(K-1).count('1')
        
        return count%2