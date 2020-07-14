#https://leetcode.com/problems/permutations/solution/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        self.comb(nums,[], out)
        return out


    def comb(self, nums, temp, out):# [1,2,3]
        if not nums:
            out.append(temp)
            return
        for elem in nums:
            new_nums = [ x for x in nums if x != elem]# [2,3]
            new_temp = [ x for x in temp]#[]
            new_temp.append(elem)#[1]
            self.comb(new_nums, new_temp, out)

