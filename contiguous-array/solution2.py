class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        map_count = {0:-1}
        max_len = 0
        for i in range(len(nums)):
            elem = nums[i]
            if not elem:
                count -= 1
            else:
                count += 1
            if count in map_count:
                max_len = max(max_len, i-map_count[count] )
            else:
                map_count[count] = i
        return max_len      
        
