class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.binary_search(nums, 0, len(nums)-1, target)
        
    def binary_search(self, nums: List[int], start:int, end:int, target:int) -> List[int]:
        if start > end:
            return [-1,-1]
        mid  = int((start+end)/2)
        if nums[mid] == target:
            first_pos = mid
            last_pos = mid
            if mid > 0 :
                if nums[mid-1] == target:
                    first_pos = self.binary_search(nums, start, mid-1, target)[0]
            if mid < len(nums)-1:
                if nums[mid+1] == target:
                    last_pos = self.binary_search(nums, mid+1, end, target)[1]
        else:
            if nums[mid] > target :
                first_pos, last_pos = self.binary_search(nums, start, mid-1, target)
            else:
                first_pos, last_pos = self.binary_search(nums, mid+1, end, target)
        return [first_pos, last_pos]
