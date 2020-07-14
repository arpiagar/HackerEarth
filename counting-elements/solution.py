

class Solution:
    def countElements(self, arr: List[int]) -> int:
        m_map = {}
        for elem in arr:
            if elem in m_map:
                m_map[elem] += 1
            else:
                m_map[elem] = 1
        count = 0
        for k in m_map.keys():
            if k+1 in m_map:
                count += m_map[k]
        return count
