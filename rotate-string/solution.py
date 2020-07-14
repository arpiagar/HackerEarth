#https://leetcode.com/problems/rotate-string/submissions/

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        if not A or not B:
            return False
        b_start = B[0]
        indices = [i for i,x in enumerate(A) if x==b_start]
        for index in indices:
            temp = [x for x in A]
            if "".join(temp[index:]+ temp[0:index]) == B:
                return True
        return False
