#https://leetcode.com/problems/3sum/submissions/
#

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out= set([])
        nums.sort()
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while(left < right):
                if nums[left]+nums[right]+nums[i] == 0:
                    out.add(tuple(sorted([nums[left],nums[right],nums[i]])))
                    left += 1
                    right -= 1
                elif nums[left]+nums[right]+nums[i] < 0:
                    left += 1
                else:
                    right -= 1
        return out

