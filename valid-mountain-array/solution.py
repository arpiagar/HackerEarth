#https://leetcode.com/problems/valid-mountain-array/submissions/


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        flag = True
        if len(A) < 2:
            return False

        if A[1] < A[0]:
            return False
        for i in range(1, len(A)-1):
            if flag:
                if A[i+1] < A[i]:
                    flag = False
                if A[i+1] == A[i]:
                    return False
            if not flag:
                if A[i+1] >= A[i]:
                    return False
        if flag:
            return False
        return True

