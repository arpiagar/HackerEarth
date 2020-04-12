#https://leetcode.com/problems/sort-colors/submissions/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        [2,0,2,1,1,0]
        0          2  0 4
        0          2  1 4
        0 0           2 4
        0 0 1  1  2 2  2 3
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums)-1
        index = 0
        while(index <= end ):
            if nums[index] == 0 :
                nums[start], nums[index] = nums[index], nums[start]
                start += 1
            elif nums[index] == 2 :
                print(index,start,end)
                nums[end], nums[index] = nums[index], nums[end]
                end -= 1
                continue
            index += 1
        return nums
