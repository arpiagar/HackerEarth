#https://leetcode.com/problems/container-with-most-water/submissions/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        m_sum = 0
        while(left < right):
            m_sum = max(m_sum,(right-left)* min(height[left],height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return m_sum
