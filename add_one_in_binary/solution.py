#https://leetcode.com/problems/add-binary/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        min_length = min(len(a), len(b))
        out = []
        carry = 0
        for i in range(min_length-1, -1, -1):
            if int(a[i]) == 1 and int(b[i]) == 1:
                if carry == 1:
                    carry = 1
                    out.append(1)
                else:
                    carry = 1
                    out.append(0)
            elif (int(a[i]) == 1 and int(b[i]) == 0) or (int(a[i]) == 0 and int(b[i]) == 1):
                if carry == 1:
                    carry = 1
                    out.append(0)
                else:
                    carry = 0
                    out.append(1)
        if len(a) > min_length:
            out+self.addtobinary(a[0:min_length], carry)
        else:
            out+self.addtobinary(b[0:min_length], carry)
        return out
    def addtobinary(self, s, carry):
        out = []
        carry = carry
        for i in range(len(s)-1, -1, -1):
            new_digit = carry + int(s[i])
            if new_digit == "2":
                carry = 1
                out.append(0)
            else:
                carry = 0
                out.append(1)
        if carry:
            out.append(1)
        return out
