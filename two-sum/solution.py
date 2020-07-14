#https://leetcode.com/problems/two-sum/submissions/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m_map = {}
        for i in range(len(nums)):
            if nums[i] in m_map:
                m_map[nums[i]].append(i)
            else:
                m_map[nums[i]] = [i]
        for k in m_map.keys():
            if target-k in m_map:
                #Handling the case where the target-k might map to k.
                if target-k == k:
                    # This should be ok in case they are 2 entries with value k.
                    if len(m_map[target-k]) > 1:
                        return m_map[target-k][0:2]
                else:
                    return [m_map[k][0], m_map[target-k][0]]
