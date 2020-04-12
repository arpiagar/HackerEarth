i#https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/submissions/
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = self.remove_extra(s, "(",")" )
        s = self.remove_extra(s[::-1], ")", "(")
        return s[::-1]

    def remove_extra(self, s, open_symbol, close_symbol):
        stack = []
        out = []
        for elem in s:
            if elem == open_symbol:
                stack.append(open_symbol)
                out.append(elem)
            elif elem == close_symbol:
                if len(stack):
                    stack.pop()
                    out.append(elem)
            else:
                out.append(elem)
        return "".join(out)
