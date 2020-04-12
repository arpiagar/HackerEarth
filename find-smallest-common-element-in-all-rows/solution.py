#https://leetcode.com/problems/find-smallest-common-element-in-all-rows/solution/

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        first_row = mat[0]
        for elem in first_row:
            flag = True
            for remaining_row_idx in range(1, len(mat)):
                remaining_row = mat[remaining_row_idx]
                if self.bs(remaining_row, elem) == -1:
                    flag = False
                    break
            if flag:
                return elem
        return -1
    def bs(self, row, element):
        return self.bs_util(row, 0, len(row)-1, element)

    def bs_util (self, row, start, end, element):
        mid = int((start+end)/2)
        if start > end:
            return -1
        if row[mid] == element:
            return mid
        if row[mid] > element:
            return self.bs_util(row, start, mid-1, element)
        else:
            return self.bs_util(row, mid+1, end, element)

