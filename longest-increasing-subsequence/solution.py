i#https://leetcode.com/problems/longest-increasing-subsequence/submissions/


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0 for x in nums]
        for i in range(len(nums)-1, -1, -1):
            max_count = 1
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    max_count = max(max_count, 1+dp[j])
            dp[i] = max_count
        return max(dp)
