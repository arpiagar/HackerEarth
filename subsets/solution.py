#https://leetcode.com/problems/subsets/solution/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = set([])
        self.recurse(0, nums,[], out)
        self.recurse(1, nums,[], out)
        return out

    def recurse(self, index, nums, temp, out):
        if index < len(nums):
            self.recurse(index+1, nums, [x for x in temp], out)
            temp.append(nums[index])
            self.recurse(index+1, nums, [x for x in temp], out)
        else:
            out.add(tuple(sorted(temp)))


