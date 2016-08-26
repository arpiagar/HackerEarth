interval_list =   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]


def condense_interval(interval_list):
	sorted_interval_list =  sorted(interval_list, key = lambda element: element[0])
	final_list = []
	if len(sorted_interval_list) > 1:
		start =  sorted_interval_list[0][0]
		end = sorted_interval_list[0][1]
		for elem in sorted_interval_list[1:]:
			if elem[0] < end:
				end = elem[1]
			else:
				final_list.append((start,end))
				start = elem[0]
				end = elem[1]
	return final_list

print condense_interval(interval_list)
