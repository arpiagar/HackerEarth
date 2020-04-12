#https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/


class Solution:
    def evaluate(self, a, b, operator):
        if operator== "+":
            return a+b
        elif operator == "-":
            return a-b
        elif operator == "*":
            return a*b
        else:
            return int(a/b)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        notation_set = {"+","*","/","-"}
        for token in tokens:
            if token in notation_set:
                elem2 = stack.pop()
                elem1 = stack.pop()
                print(elem1, elem2, token)
                ret = self.evaluate(elem1, elem2, token)
                stack.append(ret)
            else:
                stack.append(int(token))

        return stack.pop()

