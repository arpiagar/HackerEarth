#https://leetcode.com/problems/missing-element-in-sorted-array/solution/

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        missing_list = []
        index = 0
        while (len(missing_list) < k) and index<len(nums)-1:
            first_elem = nums[index]
            second_elem = nums[index+1]
            for i in range(first_elem+1, second_elem):
                missing_list.append(i)
            index += 1
        if len(missing_list) < k:
            offset = k- len(missing_list)
            return nums[-1]+offset
        else:

            return missing_list[k-1]


