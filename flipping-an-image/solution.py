#https://leetcode.com/problems/flipping-an-image/submissions/


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for rows in A:
            rows.reverse()
            for i in range(0,len(rows)):
                rows[i] = int(not rows[i])
        return A
