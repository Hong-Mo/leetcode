class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        
        stack = []
        ans = 0
        for num in A:
            left = 1
            while stack and stack[-1][0] >= num:
                n, c = stack.pop()
                ans += (n*c*left)
                left += c

            stack.append((num, left))
            print(stack)
        
        right = 1
        
        while stack :
            n, c = stack.pop()
            ans += (n*c*right)
            right += c
            
        ans = ans%(pow(10, 9)+7)
        
        return ans