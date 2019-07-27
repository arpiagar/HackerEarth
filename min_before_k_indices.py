def k_indices(input,  k):
	index_map = {}
	for i in xrange(1, len(input)):
		start_idx = i-k if (i - k > 0) else 0
		minimum = None
		for j in xrange(start_idx, i):
			if minimum == None:
				minimum = input[j]
			else:
				minimum = min(minimum, input[j])
		index_map[i] = minimum
	return index_map

print k_indices([7,8,1,11,2,5,6,7], 3)
print k_indices([], 3)
print k_indices([7,8,2], 3)
print k_indices([7,8,2,11,1,5], 3)