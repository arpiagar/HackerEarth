#https://leetcode.com/problems/longest-continuous-increasing-subsequence/submissions/

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_l = 0
        count = 0
        counter = 0
        while(counter < len(nums)-1):
            while(counter < len(nums)-1 and nums[counter] < nums[counter+1]):
                count += 1
                max_l = max(max_l,count)
                counter += 1
            count = 0
            counter += 1
        return max_l+1

