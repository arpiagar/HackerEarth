#https://leetcode.com/problems/happy-number/

class Solution:
    # 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 ->
    def isHappy(self, n: int) -> bool:
        n_map = {}
        return self.isHappyUtil(n, n_map)
    def isHappyUtil(self, n, n_map):
        if n == 1:
            return True
        if n in n_map:
            return False
        s = 0
        n_map[n] = 1
        while( n > 0):
            rem = n%10
            s += rem * rem
            n = n //10
        return self.isHappyUtil(s, n_map)
