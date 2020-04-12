#https://leetcode.com/problems/search-a-2d-matrix/submissions/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if not m:
            return False
        n = len(matrix[0])

        left, right = 0 , m*n-1

        while left <= right:
            pivot = (left+right)//2
            pivot_element = matrix[pivot // n][pivot % n]
            if target == pivot_element:
                return True
            else:
                if target > pivot_element:
                    left = pivot + 1
                else:
                    right = pivot - 1
        return False
