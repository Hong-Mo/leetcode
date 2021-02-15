class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0

        nee_len = len(needle)

        for i in range(0, len(haystack) - nee_len + 1):
            if haystack[i:(i+nee_len)] == needle:
                return i

        return -1