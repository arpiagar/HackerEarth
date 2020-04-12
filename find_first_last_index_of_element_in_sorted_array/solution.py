#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        return self.searchStartEnd2(nums, start, end, target)


    def searchStartEnd2(self, nums, start, end, target):
        ret_start = end_start = -1
        mid  = int((start+end)/2)
        if end >= start: #Important test case since when start==end, element needs to be validated for.
            if nums[mid] == target:
                ret_start, k = self.searchStartEnd2(nums, start, mid-1, target)
                k, ret_end = self.searchStartEnd2(nums, mid+1, end, target)
                if ret_start != -1:
                    if ret_end != -1:
                        return ret_start, ret_end
                    else:
                        return ret_start, mid
                else:
                    if ret_end != -1:
                        return mid, ret_end
                    else:
                        return mid, mid
            else:
                if nums[mid] > target:
                    return self.searchStartEnd2(nums, start, mid-1, target)
                else:
                    return self.searchStartEnd2(nums, mid+1, end, target)
        else:
            return -1,-1
