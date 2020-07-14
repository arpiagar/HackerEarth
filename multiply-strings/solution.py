#https://leetcode.com/problems/multiply-strings/submissions/



class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        t_len = len(num1) + len(num2) + 1
        out = [0 for x in range(t_len)]
        num1 = [int(x) for x in num1]
        num2 = [int(x) for x in num2]
        num1 = num1[::-1]
        num2 = num2[::-1]
        product = 0
        carry = 0

        for i in range(len(num1)):
            for j in range(len(num2)):
                product += num2[j] * pow(10,i)*num1[i]*pow(10,j)

        return str(product)
