#https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_offset = 0
        col_offset = 0
        n_rows = len(matrix)
        n_col = len(matrix[0])
        for i in range(0, int(n_rows/2)):        



    def getRow(self, row_id, col_offset, matrix, n_rows, n_col):
        out = []
        for i in range(0+col_offset, n_col-col_offset):
            out.append(matrix[row_id][i]
        return out

    def getCol(self, col_id, row_offset, matrix, n_rows, n_col):
        out = []
        for i in range(0+row_offset, n_rows-row_offset):
            out.append(matrix[i][col_id]
        return out


