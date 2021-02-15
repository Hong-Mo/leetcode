class Solution:
    def climbStairs(self, n: int) -> int:
            if n <= 2:
                return n
            else:
                sum = 0
                a = 1
                b = 2 

                for i in range(0, n-2):
                    sum = a + b 
                    a = b
                    b = sum
            return sum