def check(curr_path,start_i,start_j):
	if (start_i,start_j) in curr_path:
		return True
	else:
		return False

def count_path(ip,strt_i,strt_j,end_i,end_j,path_count,count,curr_path):
	if count == 0:
		count_path += 1
		return 
	if strt_i+1 < end_i:
		if check(curr_path,strt_i+1,strt_j):
			new_curr_path = [x for x in curr_path]
			new_curr_path.append((strt_i+1, strt_j))
			path_count =  count_path(ip,strt_i+1,strt_j,end_i,end_j,count_path,count,new_curr_path)
	if strt_j+1 < end_j:
		if check(curr_path,strt_i,strt_j+1):
			new_curr_path = [x for x in curr_path]
			new_curr_path.append((strt_i, strt_j+1))
			path_count =  count_path(ip,strt_i,strt_j+1,end_i,end_j,count_path,count,new_curr_path)
	if strt_i-1 >= 0 :
		if check(curr_path,strt_i-1,strt_j):
			new_curr_path = [x for x in curr_path]
			new_curr_path.append((strt_i-1, strt_j))
			path_count =  count_path(ip,strt_i-1,strt_j,end_i,end_j,count_path,count,new_curr_path)
	if strt_j-1 >= 0:
		if check(curr_path,strt_i,strt_j-1):
			new_curr_path = [x for x in curr_path]
			new_curr_path.append((strt_i, strt_j-1))
			path_count =  count_path(ip,strt_i,strt_j-1,end_i,end_j,count_path,count,new_curr_path)
	if strt_i+1 < end_i and start_j-1 >= 0:
		if check(curr_path,strt_i+1,strt_j-1):
			new_curr_path = [x for x in curr_path]
			new_curr_path.append((strt_i+1, strt_j-1))
			path_count =  count_path(ip,strt_i+1,strt_j-1,end_i,end_j,count_path,count,new_curr_path)
	if strt_i+1 < end_i and start_j+1 < end_j:
		if check(curr_path,strt_i+1,strt_j+1):
			new_curr_path = [x for x in curr_path]
			new_curr_path.append((strt_i+1, strt_j+1))
			path_count =  count_path(ip,strt_i+1,strt_j+1,end_i,end_j,count_path,count,new_curr_path)
	if strt_i-1 >=0  and start_j-1 >= 0: :
		if check(curr_path,strt_i-1,strt_j-1):
			new_curr_path = [x for x in curr_path]
			new_curr_path.append((strt_i-1, strt_j-1))
			path_count =  count_path(ip,strt_i-1,strt_j-1,end_i,end_j,count_path,count,new_curr_path)
	if strt_i-1 >= 0 and start_j+1 < end_j:
		if check(curr_path,strt_i-1,strt_j+1):
			new_curr_path = [x for x in curr_path]
			new_curr_path.append((strt_i-1, strt_j+1))
			path_count =  count_path(ip,strt_i-1,strt_j+1,end_i,end_j,count_path,count,new_curr_path)
	return path_count






def find_combination(input_array, m,n):
	MAX_COUNT = m*n
	path_num = 0
	for i in xrange(0,n):
		for j in xrange(0,m):
			for count in xrange(0,MAX_COUNT):
				count_path(input_array,i,j,n,m,count_path,count,[]])





