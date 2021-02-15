class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(0, len(coordinates)-1):
            x_gap = coordinates[i][0]-coordinates[i+1][0]
            y_gap = coordinates[i][1]-coordinates[i+1][1]
            
            if x_gap!= 0:
                slope = y_gap/x_gap
            
            else:
                slope = 'vertical'
            
            if i==0:
                check = slope
                continue
            
            if slope!=check:
                return False
        
        return True