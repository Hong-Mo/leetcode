class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zig = []

        for i in range(0, numRows):
            zig.append([])

        start = 0
        judge = 1

        if numRows == 1:
            return s


        for i in range(0, len(s)):
            zig[start].append(s[i])
            if judge == 1 :
                start += 1
            else:
                start -= 1

            if start == 0:
                judge = 1
            elif start == numRows-1:
                judge = 0

        zigstr = ''

        for r in zig :
            for c in r:
                zigstr += c

        return zigstr