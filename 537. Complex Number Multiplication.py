class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a, b= a.split('+'), b.split('+')
        a[1], b[1] = a[1][:-1], b[1][:-1]
        
        a[:], b[:] = [int(n) for n in a], [int(n) for n in b]
        
        real = (a[0]*b[0])-(a[1]*b[1])
        im = (a[0]*b[1])+(b[0]*a[1])
        
        return str(real)+'+'+str(im)+'i'