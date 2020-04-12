#https://leetcode.com/problems/add-binary/solution/
def add(n1,n2,carry):
    num = n1+n2+carry
    if num == 0:
        num, carry = 0,0
    elif num == 1:
        num , carry = 1,0
    elif num == 2:
        num , carry = 0,1
    else:
        num, carry = 1,1
    return num,carry
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l1 = len(a)
        l2 = len(b)
        carry = 0
        length = min(l1,l2)
        a = a[::-1]
        b = b[::-1]
        out=[]
        print(a,b)
        for i in range(length):
            num, carry = add(int(a[i]),int(b[i]),carry)
            print(out,num,carry)
            out.append(num)
        if l1 > l2:
            for i in range(l2,l1):
                num ,carry = add(int(a[i]) ,0,carry)
                out.append(num)
        else:
            for i in range(l1,l2):
                num, carry = add(0,int(b[i]),carry)
                out.append(num)
        if carry:
            out.append(carry)
        out = out[::-1]
        out = [str(x) for x in out]
        return "".join(out)
                
