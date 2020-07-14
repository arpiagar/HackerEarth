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
        print(row,col)
        min_col = -1
        col_len = col-1
        for i in range(row):
            idx = self.bs(0, col_len, i, binaryMatrix )
            print(idx)
            if idx != -1:
                min_col = idx
                col_len = idx
        return min_col
                
    def bs(self, left, right, row, binaryMatrix):
        min_idx =-1
        while(left <= right):
            mid = (left+right)//2
            if binaryMatrix.get(row, mid) == 0:
                left =mid+1
            else:
                min_idx = mid
                right = mid-1
        return min_idx
    
                
