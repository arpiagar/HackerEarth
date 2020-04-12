#https://leetcode.com/problems/search-insert-position/solution/


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        return self.find_in_array(nums, target, start, end)


    def find_in_array(self, nums, target, start, end):
        mid = int((start+end)/2)
        if start > end:
            return start
        if nums[mid] == target:
            return mid
        if target > nums[mid]:
            return self.find_in_array(nums, target, mid+1, end)
        else:
            return self.find_in_array(nums , target, start, mid-1)

