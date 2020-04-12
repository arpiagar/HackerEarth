i#https://leetcode.com/problems/squares-of-a-sorted-array/submissions/
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        N = len(A)
        second_index = 0
        while second_index<N and A[second_index] < 0:
            second_index += 1
        first_index = second_index-1
        ans = []
        print(first_index,second_index)
        while( first_index>=0 and second_index<N):
            if A[second_index]**2 > A[first_index]**2:
                ans.append(A[first_index]**2)
                first_index -=1
            else:
                ans.append(A[second_index]**2)
                second_index += 1


        while(first_index >=0):
            ans.append(A[first_index]**2)
            first_index -= 1
        while(second_index <N):
            ans.append(A[second_index]**2)`
            second_index += 1
        return ans

    def sortedSquares1(self, A: List[int]) -> List[int]:
        return sorted([ x*x for x in A])
