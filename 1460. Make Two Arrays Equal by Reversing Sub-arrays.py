class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        num_tar = [0]*1000
        num_arr = [0]*1000
        
        for num in target:
            num_tar[num-1] +=1
            
        for num in arr:
            num_arr[num-1] +=1
        
        if num_tar == num_arr:
            return True
        
        return False