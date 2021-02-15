class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        judge = 0
        

        for i in range(0, len(A)-1):
            if judge == 0 :

                if A[i] < A[i+1] :
                    judge = 1

                elif A[i] > A[i+1]:
                    judge = 2


            elif judge == 1:

                if A[i] > A[i+1]:
                    return False

            else:

                if A[i] < A[i+1]:
                    return False

        return True