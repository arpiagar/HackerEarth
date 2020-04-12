#https://leetcode.com/problems/plus-one/submissions/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        offset = 1
        out_list = []
        for i in range(len(digits)-1, -1, -1):
            digit = int(digits[i])
            new_digit = digit + offset + carry
            offset = 0
            if new_digit == 10:
                carry = 1
                out_list.append(0)
            else:
                out_list.append(new_digit)
                carry = 0
        if carry == 1:
            out_list.append(1)
        out_list.reverse()
        return out_list

