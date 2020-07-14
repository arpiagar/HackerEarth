#https://leetcode.com/problems/search-in-rotated-sorted-array-ii/submissions/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums)-1
        return self.searchUtil(nums, start, end, target)


    def searchUtil(self, nums, start, end, target):
        while(start<=end):
            mid = (start+end)//2
            if nums[mid] == target:
                return True
            if nums[start] == nums[mid]:
                return self.searchUtil(nums, start, mid-1, target) or self.searchUtil(nums,mid+1,end,target)
            if nums[start] > nums[mid]:
                if target < nums[start] and target > nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
            else:
                if target >= nums[start] and target < nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
        return False


# 1 3 1 1 1
# 1 1 1 3 1
