class Solution:
    def gcd(self, a, b):
        if b==0:
            return a
        
        return self.gcd(b, a%b)
    
    def lcm(self, a,b):
        return (a*b)//self.gcd(a,b)
    
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        A, B, AB_lcm = min(A,B), max(A,B), self.lcm(A, B)
        mutiple, addtional, turn = 0, 0, sum([AB_lcm//A, AB_lcm//B])-1

        quo, N = divmod(N, turn)
        mutiple += quo*AB_lcm
        
        if N:
            if B%A==0:
                addtional = (A*N)
            
            else:
                step = (B/A)+1
                sec = int(N//step)
                cur, val, bound = sec + (B*sec)//A, B*sec, (B*(sec+1))

                while cur<N:
                    addtional = min(((val//A)+1)*A, bound)
                    val, cur = addtional, cur+1
        
        return (mutiple+addtional)%(pow(10, 9)+7)