#https://leetcode.com/problems/monotonic-array/submissions/

class Solution:
    def isMon(self, A, flag):
        if not A:
            return True
        temp = A[0]
        if flag:
            for i in range(1, len(A)):
                if temp > A[i]:
                    return False
            return True
        else:
            for i in range(1, len(A)):
                if temp < A[i]:
                    return False
            return True

    def isMonotonic(self, A: List[int]) -> bool:
        if not A:
            return True

        flag = None
        i=0
        while(i < len(A)-1):
            if A[i] < A[i+1]:
                return self.isMon(A[i+1:], True)
            if A[i] > A[i+1]:
                return self.isMon(A[i+1:], False)
            i+=1
        return True
