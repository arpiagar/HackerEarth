#https://leetcode.com/problems/backspace-string-compare/solution/


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        out1 = []
        out2 = []
        for elem in S:
            if elem == "#":
                if len(out1):
                    out1 = out1[:-1]
            else:
                out1.append(elem)

        for elem in T:
            if elem == "#":
                if len(out2):
                    out2=out2[:-1]
            else:
                out2.append(elem)
        print(out1, out2)

