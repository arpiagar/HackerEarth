#https://leetcode.com/problems/continuous-subarray-sum/submissions/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        summ = 0
        for i in range(len(nums)):
            summ = nums[i]
            for j in range(i+1, len(nums)):
                summ += nums[j]
                if  k==0 and summ == 0:
                    return True
                if k!=0 and summ % k == 0:
                    print(summ)
                    return True
        return False
