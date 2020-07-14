#https://leetcode.com/problems/reverse-integer/submissions/

class Solution:
    def reverse(self, x: int) -> int:
        s_max, s_min= pow(2,31)-1, pow(2,31)*-1

        if x == 0:
            return x
        flag = False
        if x < 0:
            x = x* -1
            flag = True
        num = 0
        while(x):
            rem = x % 10
            x = x // 10
            if num > s_max/10:
                return 0
            num = num*10 + rem

        if flag:
            return num*-1
        return num


