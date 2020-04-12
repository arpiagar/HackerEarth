#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left != right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                if right-mid == 1:
                    return nums[right]
                left = mid
            else:
                right = mid
        return nums[left]

