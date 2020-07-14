class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [2,0,2,1,1,0]  0,5   [0,0,2,0,1,2] 0,4 [0,0,1,1,2,2] 2,3
        # [2,0,2,0,1,0] 0,5 [0,0,2,0,1,2]  1,4,1  [0,0,1,0,2,2] 2,4,3, [0,0,0,1,2,2]
        left = 0  
        right = len(nums)-1
        counter = 0
        while(counter <= right):
            if nums[counter] == 0:
                nums[counter], nums[left] = nums[left], nums[counter]
                left += 1
                counter += 1
            elif nums[counter] == 1:
                counter += 1
            else:
                nums[counter], nums[right] = nums[right], nums[counter]
                right -= 1
        
