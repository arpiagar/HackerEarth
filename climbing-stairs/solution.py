#https://leetcode.com/problems/climbing-stairs/submissions/

class Solution:
    def climbStairs(self, n: int) -> int:
        m_map={}
        m_map[0] = 1
        return self.climb(n, m_map)

    def climb(self, n, m_map):
        if n in m_map:
            return m_map[n]
        if n<0:
            return 0
        else:
            m_map[n] = self.climb(n-1, m_map)+self.climb(n-2, m_map)
            return m_map[n]


