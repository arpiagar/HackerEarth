# https://leetcode.com/problems/3sum/submissions/

class Solution:

    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        m_map = {}
        out = set([])
        num_list = list(set(nums))
        if len(num_list) == 1 and len(nums) >=3:
            if num_list[0] == 0:
                return [[0,0,0]]
            else:
                return out
        for elem in nums:
            if elem in m_map:
                m_map[elem] += 1
            else:
                m_map[elem] = 1
        print(m_map)
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                count = 1
                check_elem = (nums[i] + nums[j]) * -1
                if check_elem == nums[i] or check_elem == nums[j]:
                    if nums[i] == nums[j]:
                        count = 3
                    else:
                        count = 2
                if check_elem in m_map:
                    if m_map[check_elem] >= count:
                        out.add(tuple(sorted([nums[i],nums[j],check_elem])))
        return list(out)
