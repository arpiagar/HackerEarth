'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
first_row = raw_input().split(' ')
n,m  = [int(x) for x in first_row]

input_array = []

for i in xrange(0,n):
  input_list = raw_input().split(' ')
  input_array.append([int(x) for x in input_list])

path_list = []

def find_path(input_array,x_start, y_start, x_end, y_end, curr_path, path_list):
  if x_start+1 <= x_end:
    new_path =  [x for x in curr_path]
    new_path.append(input_array[x_start+1][y_start])
    find_path(input_array,x_start+1, y_start, x_end, y_end, new_path, path_list)
  if y_start+1 <= y_end:
    new_path =  [x for x in curr_path]
    new_path.append(input_array[x_start][y_start+1])    
    find_path(input_array,x_start, y_start+1, x_end, y_end, new_path, path_list)
  elif x_start==x_end and y_start==y_end:
    path_list.append(curr_path)

x_start, y_start, x_end, y_end = 0,0,n-1,m-1

find_path(input_array,x_start, y_start, x_end, y_end, [input_array[x_start][y_start]], path_list)

min_sum = sum(path_list[0])
index = 0
for i in xrange(1,len(path_list)):
  if sum(path_list[i]) < min_sum:
    index = i
    min_sum = sum(path_list[i])

path_list[index].sort()
print [x for x in path_list[index]]

	
