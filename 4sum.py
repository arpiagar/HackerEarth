class Solution(object):
    def fourSum(self, nums, target):
    	output = []
    	for i in xrange(0 , len(nums)):
    		self.recurse(i+1, nums, 3, target-nums[i], [nums[i]], output)
    		self.recurse(i+1, nums, 4, target, [], output)
    	return list(set(output))


    def recurse(self, index, nums, count, current_target, current_list, output):
    	if count == 0:
    		print current_target, current_list, output
    		if current_target == 0:
    			current_list.sort()
    			output.append(tuple(current_list))
    		else:
    			return 
    	else:
    		if index < len(nums):
    			current_list2 = [x for x in current_list]
    			current_list.append(nums[index])
    			self.recurse(index+1, nums, count-1, current_target-nums[index], current_list, output)
    			self.recurse(index+1, nums, count, current_target, current_list2, output)
    		else:
    			return

    def fourSumHashMap(self, nums, target):
    	nums_map = {}
    	output = []
    	for i in xrange(0, len(nums)):
    		for j in xrange(i+1, len(nums)):
    			if not nums_map.has_key(nums[i]+nums[j]):
    				nums_map[nums[i]+nums[j]] = [(i,j)]
    			else:
    				nums_map[nums[i]+nums[j]].append((i,j))

    	for elem in nums_map.keys():
    		if nums_map[target-elem]:
    			unique, out_array = self.unique(nums_map,elem, target-elem)
    			if unique:
    				output = output + out_array

    	return output


    def unique(self, nums_map, elem1, elem2 ):
    	 first_list = nums_map[elem1]
    	 second_list = nums_map[elem2]
    	 print first_list,second_list
    	 first_map = {}
    	 for elem in first_list:
    	 	first_map[elem] = 1
    	 out_list = []
    	 flag = 0
    	 for elem in second_list:
    	 	if not first_map.has_key(elem):
    	 		flag = 1
    	 		out_list.append(elem)

    	 return flag, out_list


if __name__ == "__main__":
	s = Solution()
	print s.fourSum([0,0,0,0], 0)
	print s.fourSumHashMap([0,0,0,0], 0)

