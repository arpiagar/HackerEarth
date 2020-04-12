#https://leetcode.com/problems/toeplitz-matrix/submissions/
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n  = len(matrix[0])
        for i in range(0, m):
            j = 0
            temp_set = set()
            while(i< m and j < n):
                temp_set.add(matrix[i][j])
                i += 1
                j += 1
            if len(temp_set) > 1:
                return False
        for i in range(0, n):
            j = 0
            temp_set=set()
            while(i<n and j <m):
                temp_set.add(matrix[j][i])
                i+=1
                j+=1
            if len(temp_set) > 1:
                return False
        return True

