

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        array_map = {}
        summ = 0
        count = 0
        array_map[0] = 1
        for elem in nums:
            summ  += elem
            if summ-k in array_map:
                count += array_map[summ-k]
            if summ in array_map:
                array_map[summ] += 1
            else:
                array_map[summ] = 1
        return count

    def subarraySum2(self, nums: List[int], k: int) -> int:
        combination_count = 0
        cumulative_sum = [0 for x in range(len(nums)+1)]
        if not nums:
            return 0
        cumulative_sum[0] = 0
        for i in range(1, len(nums)+1):
            cumulative_sum[i] = cumulative_sum[i-1]+ nums[i-1]

        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                if cumulative_sum[j]-cumulative_sum[i] == k:
                    combination_count += 1
        return combination_count



# [1,2,3,4], [1,3,6,10]
    def subarraySum1(self, nums: List[int], k: int) -> int:
        combination_count = 0
        for i in range(len(nums)):
            k_sum = nums[i]
            if k_sum == k:
                combination_count += 1
            j = i+1
            while(j < len(nums)):
                k_sum += nums[j]
                j +=1
                if k_sum == k:
                    combination_count += 1
        return combination_count

