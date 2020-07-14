

class Solution:
    def checkValidString(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        s = [x for x in s]
        return self.valid2(s, 0, 0)


    def valid2(self, s, idx , count):
        if idx > len(s)-1:
            return count == 0
        if count < 0 :
            return False
        if s[idx] == '(':
            count += 1
            return self.valid2(s, idx+1, count)
        if s[idx] == ')':
            count -= 1
            return self.valid2(s, idx+1, count)
        if s[idx] == '*':
            return self.valid2(s, idx+1, count) or self.valid2(s, idx+1, count+1) or self.valid2(s, idx+1, count-1)

