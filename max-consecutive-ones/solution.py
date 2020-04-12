#https://leetcode.com/problems/max-consecutive-ones/submissions/


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for elem in nums:
            if elem:
                count += 1
                max_count = max(count,max_count)
            else:
                count = 0
        return max_count
        
