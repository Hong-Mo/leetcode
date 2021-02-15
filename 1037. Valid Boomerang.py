class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1_gap = points[0][0] - points[1][0]
        x2_gap = points[1][0] - points[2][0]
        
        y1_gap = points[0][1] - points[1][1]
        y2_gap = points[1][1] - points[2][1]
        
        try:
            if (y1_gap/x1_gap) == (y2_gap/x2_gap):
                return False
        
        except :
            if (x1_gap == x2_gap) or (points[0] == points[1]) or (points[1] == points[2]):
                return False
        
        return True