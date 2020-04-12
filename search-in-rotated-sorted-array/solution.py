i#https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        idx = self.find_rotated_index(nums, 0, len(nums)-1)
        if nums[0] <= target <= nums[idx]:
            left = 0
            right = idx
        else:
            left,right = idx+1, len(nums)-1

        while left <= right:
            mid = (left+right)//2
            print("mid",nums[mid])
            if target == nums[mid]:
                print("target", mid)
                return mid
            if target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return -1


    def find_rotated_index(self, nums, start, end):
        mid = (start+end) // 2
        if nums[start] < nums[end]:
            return 0
        if nums[mid] > nums[mid+1]:
            return mid
        if nums[mid] > nums[end]:
            return self.find_rotated_index(nums,mid, end)
        elif nums[start] > nums[mid]:
            return self.find_rotated_index(nums, start, mid)































