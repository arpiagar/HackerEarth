# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()
        col_idx = col-1
        for i in range(row):
            print(i,col_idx)
            while(col_idx>=0 and binaryMatrix.get(i,col_idx) == 1):
                col_idx -= 1
        print(col_idx)
        if col_idx == col-1:
            return -1
        return col_idx+1
