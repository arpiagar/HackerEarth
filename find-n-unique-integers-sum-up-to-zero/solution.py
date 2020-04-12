i#https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/submissions/

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        if n%2:
            start = [-1,0,1]
        else:
            start = [-1,1]
        divisor = int(n/2)
        for i in range(0, divisor-1):
            start.append(i+2)
            start.append(-i-2)
        return start
