class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-2, -1, -1):
            swap = [i, 0]
            
            for j in range(i+1, len(arr)):
                if arr[j]>swap[1] and arr[j]<arr[i]:
                    swap[:] = [j, arr[j]]
            
            if swap[0]!=i:
                arr[i], arr[swap[0]] = arr[swap[0]], arr[i]
                break
        
        return arr