#https://leetcode.com/problems/count-square-submatrices-with-all-ones/submissions/


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        if not matrix or not matrix[0]:
            return count
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        for i in range (n_rows):
            for j in range(n_cols):
                count += self.availableSquares(matrix, i, j, n_rows, n_cols)
        return count

    def availableSquares(self, matrix, i, j, n_rows, n_cols):
        count = 0
        row_counter = i
        col_counter = j
        for k in range(0, max(n_rows,n_cols)):
            if row_counter+k < n_rows and col_counter+k < n_cols and matrix[row_counter+k][col_counter+k] == 1:
                if self.checkAllOnes(matrix, row_counter,col_counter,row_counter+k,col_counter+k):
                    count += 1
                else:
                    break
        return count

    def checkAllOnes(self, matrix, startx,starty,endx,endy):
        for i in range(startx, endx+1):
            for j in range(starty, endy+1):
                if matrix[i][j] != 1:
                    return False
        return True
