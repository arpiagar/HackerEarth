#https://leetcode.com/problems/jump-game




class Solution:
    def canJump(self, nums: List[int]) -> bool:
        per_map = {}
        return self.jump(nums, 0, len(nums)-1, per_map)

    def jump(self, nums, index, n, per_map):
        if index in per_map:
            return per_map[index]
        if n == index:
            per_map[index] = True
        elif index > n:
            per_map[index] = False
        else:
            count = nums[index]
            count = min(n, count)
            flag = False
            for i in range(count, 0, -1):
                if index+i <= n:
                    flag = flag or self.jump(nums, index+i, n, per_map)
                if flag:
                    per_map[index] = flag
                    return flag
            per_map[index] = flag
        return per_map[index]
