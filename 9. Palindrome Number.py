class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        l = len(x_str) - 1

        for i in range(0, len(x_str)//2):
            if x_str[i] != x_str[l]:
                return False
            l = l - 1

        return True