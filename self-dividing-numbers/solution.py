#https://leetcode.com/problems/self-dividing-numbers/solution/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        out = []
        for i in range(left, right+1):
            if str(i).find("0") == -1 and self.dividingNumber(i):
                out.append(i)
        return out

    def dividingNumber(self, num):
        divisor = int(num/10)
        rem = num % 10
        print(num, divisor, rem)
        if int(num % rem) != 0:
            return False
        while (divisor != 0):
            temp = divisor
            divisor = int(temp /10)
            rem = temp % 10
            print(num, divisor, rem)
            if int(num % rem) != 0:
                return False
        return True
