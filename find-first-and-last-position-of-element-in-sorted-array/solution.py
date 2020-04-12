#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.search(nums, target, 0 , len(nums)-1)

    def search(self, nums, target, start, end):
        if start > end:
            return [-1, -1]
        mid  =  (start+end)//2
        if nums[mid] == target:
            min_idx, max_idx = mid, mid
            min_idx, temp = self.search(nums, target, start, mid-1 )
            if min_idx == -1:
                min_idx = mid
            temp, max_idx = self.search(nums, target, mid+1, end )
            if max_idx == -1:
                max_idx = mid
        else:
            if nums[mid] > target:
                min_idx, max_idx = self.search(nums, target, start, mid-1 )
            else:
                min_idx, max_idx = self.search(nums, target, mid+1, end )
        return [min_idx, max_idx]
