#https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        b = "0"*(32-len(bin(n)[2:]))+bin(n)[2:]
        return int("".join(b[::-1]),2)
