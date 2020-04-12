https://leetcode.com/problems/evaluate-reverse-polish-notation/


import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_map = {"+":operator.add, "-":operator.sub,"*":operator.mul, "/": 1}
        if len(tokens) == 1:
            return tokens[0]
        for i in range(0, len(tokens)):
            elem  = tokens[i]
            if elem in op_map:
                if elem == "/":
                    num = int(int(tokens[i-2])/int(tokens[i-1]))
                else:
                    num  = op_map[elem](int(tokens[i-2]), int(tokens[i-1]))
                new_token = tokens[0:i-2] +[num]+ tokens[i+1:]
                return self.evalRPN(new_token)





