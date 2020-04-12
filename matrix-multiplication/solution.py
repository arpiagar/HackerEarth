#https://leetcode.com/problems/sparse-matrix-multiplication/

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not len(A):
            return []
        A_col = len(A[0])
        B_row = len(B)
        out = []
        for i in range(0, len(A) ):
            temp = []
            for k in range(0, len(B[0])):
                val = 0
                for j in range(0, len(A[0])):
                    val += A[i][j]*B[j][k]
                temp.append(val)
            out.append(temp)

        return out

