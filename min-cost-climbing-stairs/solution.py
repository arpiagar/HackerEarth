#https://leetcode.com/problems/min-cost-climbing-stairs/submissions/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        m_map ={}
        return min(self.minCost(cost, 0, len(cost), 0, m_map),
                       self.minCost(cost, 1, len(cost), 0, m_map))

    def minCost(self, cost, idx, n, ssum,m_map):
        if idx in m_map:
            return m_map[idx]
        if idx >=n :
            return 0
        else:
            m_map[idx] = cost[idx] + min(self.minCost(cost, idx+1, n, cost[idx],m_map),
                       self.minCost(cost, idx+2, n, cost[idx],m_map))
            return m_map[idx]
