i#https://leetcode.com/problems/next-closest-time/submissions/


class Solution:
    def nextClosestTime(self, time: str) -> str:
        hh, mm = time.split(":")
        digits = list(set([x for x in time if x!=":"]))
        max_mm = self.findClosestWithinRange(0, 59, mm, digits)
        print(max_mm)
        if int(max_mm) < int(mm):
            new_hh = self.findClosestWithinRange(0, 23, hh, digits)
            return ":".join([new_hh,max_mm])
        else:
            return ":".join([hh,max_mm])


    def findClosestWithinRange(self, range_start, range_end,current, digits):
        last_digit = int(current[-1])
        digits = [int(x) for x in digits]
        sorted_digits = sorted(digits)
        print(last_digit, sorted_digits)
        for digit in sorted_digits:
            if digit > last_digit and range_start<= 10*int(current[0])+digit<=range_end:
                return current[0]+str(digit)
        second_last_digit = int(current[-2])
        for digit in sorted_digits:
            if digit > second_last_digit:
                if range_start <= 10*digit+sorted_digits[0] <= range_end:
                    return str(10*digit+sorted_digits[0])
        return str(sorted_digits[0])+str(sorted_digits[0])

