#https://leetcode.com/problems/valid-parentheses/submissions/

class Solution:
    
    def isValid(self, s: str) -> bool:
        stack = [] # "[([]])"
        for elem in s:
            if not stack:
                stack.append(elem) # [ ( [ 
            else:
                if elem in [')','}',']']:
                    stack_elem = stack.pop()
                    if elem == ')' and stack_elem != '(':
                        return False
                    if elem == '}' and stack_elem != '{':
                        return False
                    if elem == ']' and stack_elem != '[':
                        return False
                else:
                    stack.append(elem) 
        if not stack:
            return True
        return False
