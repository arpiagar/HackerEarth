#https://leetcode.com/problems/fibonacci-number/submissions/

class Solution:
    def fib(self, N: int) -> int:
        m_map = {0:0,1:1}
        return self.fibI(N)
        return self.fibR(N, m_map)

    def fibR(self, n , m_map):
        if n in m_map:
            return m_map[n]
        m_map[n] = self.fibR(n-1, m_map) + self.fibR(n-2, m_map)
        return m_map[n]

    def fibI(self, n):
        prev = 0
        curr = 1
        if n == 0 or n==1:
            return n
        count = 1
        while(count <= n):
            curr, prev = curr + prev, curr
            count += 1
        return prev


