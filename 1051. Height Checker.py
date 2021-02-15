class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sort = heights[:]
        heights_sort.sort()


        reorder = 0

        for i in range(0, len(heights)):

            if heights[i] != heights_sort[i]:
                reorder += 1

        return reorder