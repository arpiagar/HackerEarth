#https://leetcode.com/problems/n-th-tribonacci-number/submissions/


class Solution:
    def tribonacci(self, n: int) -> int:
        m_map = {0:0,1:1,2:1}
        return self.triboR(n, m_map)

    def triboR(self, n, m_map):
        if n in m_map:
            return m_map[n]
        else:
            m_map[n] = self.triboR(n-1, m_map)+self.triboR(n-2, m_map)+self.triboR(n-3, m_map)
            return m_map[n]
