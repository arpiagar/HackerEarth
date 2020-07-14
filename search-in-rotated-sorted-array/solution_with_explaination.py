#https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

# [5,1,3]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        # Equality because when subarray looks like
        #[3,4] left = 0, right=1 ,target= 4, mid=0
        #then one would set left to mid+1 which means
        #left==right. This would not be evaluated if
        #we have left<right.
        while(left<=right):

            mid = (left+right)//2
            if nums[mid]== target:
                return mid
            #We start with the case where we know for sure the rotated index
            #exists. wherever rotated index, nums[left] > nums[mid].Try any
            #permuation
            if nums[left] > nums[mid]:
                #So now we now rotated index exists between left and mid,
                #so we want to evaluate whether target exists in the other half.
                # so if target < nums[left] along with target >nums[mid], we are
                #sure it would not exist between left and mid and hence we move
                # the left to mid+1
                if target < nums[left] and target > nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                #This is the case where the sequence is sorted and we ensure
                #target >= nums[start] and target < nums[mid]. We do not have
                #equality for nums[mid] since nums[mid] is already evaluated in the
                #first step.
                if target >= nums[left] and target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
        return -1


