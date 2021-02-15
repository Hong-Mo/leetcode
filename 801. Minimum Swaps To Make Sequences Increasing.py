class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        l = len(A)
        swap, not_swap = [l]*l, [l]*l
        swap[0] = 1
        not_swap[0] = 0
        
        for i in range(1, l):
            if A[i-1]<B[i] and B[i-1]<A[i]:#此種情況, 保證increasing, A[i]和B[i]交換, 或者A[i-1]和B[i-1]交換
                not_swap[i] = swap[i-1]
                swap[i] = not_swap[i-1]+1
                
            if A[i-1]<A[i] and B[i-1]<B[i]:#此種情況, 保證increasing, 都不交換, 或者都交換, 且若兩種情況都符合的話, 取min
                not_swap[i] = min(not_swap[i], not_swap[i-1])
                swap[i] = min(swap[i], swap[i-1]+1)
            
        return min(not_swap[-1], swap[-1]) #最後返回最小值