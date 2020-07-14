#https://leetcode.com/problems/contiguous-array/

class Solution:
    # 0 0 1 0 0 0 1 1 1  0 0 1
    def findMaxLength(self, nums: List[int]) -> int:
        nr_z = nr_o = 0
        out = [0 for x in nums]
        for i in range(len(nums)):
            if nums[i] == 0:
                nr_z += 1
            else:
                nr_o += 1
            out[i] = nr_z-nr_o
        d_map = {}
        max_c = 0
        for i in range(len(out)):
            elem = out[i]
            # if the different between count of 0 and 1 is 0, that means there
            # are equal 0 and 1 when counted from start.
            if elem == 0:
                max_c = max(max_c, i+1)
                continue
            ## This is the case where the counting starts from some random
            # index i.
            if elem in d_map:
                d_map[elem].append(i)
            else:
                d_map[elem] = [i]

        for v in d_map.values():
            if len(v) > 1:
                max_c = max(max_c, v[-1]-v[0])
        return max_c
