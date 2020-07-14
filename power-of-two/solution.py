#https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n==1:
            return True
        else:
            rem = n%2
            if rem:
                return False
            n = n//2
            return self.isPowerOfTwo(n)

