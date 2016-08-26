# breakfast beach citycenter location metro view staff price
# 5
# 1
# This hotel has a nice view of citycenter. The location is perfect
import operator

word_list = raw_input().split(" ")
word_list = [x.lower().strip(',').strip('.') for x in word_list]
num =  int(raw_input())
init_map = {}
for i in xrange(0,num):
  index =  int(raw_input())
  input_string = raw_input()
  if init_map.has_key(index):
    init_map[index].append(input_string.lower().split(" "))
  else:
    init_map[index] = [input_string]

out_map = {}
for k,v in init_map.iteritems():
  for reviews in v:
    for elem in word_list:
      if elem in reviews:
        if out_map.has_key(k):
          out_map[k] += 1
        else:
          out_map[k] = 1

out_list_sorted = sorted(out_map.items(), key=operator.itemgetter(1))
out_list_sorted.reverse()
prev_key =  None
prev_value =  None
output = []
prev_index_list = []
for elem in out_list_sorted:
  if prev_key == None:
    prev_key,prev_value = elem[0],elem[1]
    prev_index_list = [elem[0]]
  else:
    if prev_value == elem[1]:
      prev_index_list.append(elem[0])
    else:
      sorted_list = sorted(prev_index_list)
      for element in sorted_list:
        output.append(element)
      prev_index = elem[0]
      prev_value = elem[1]
      prev_index_list = [elem[0]]




output = [str(x[0]) for x in out_list_sorted]

print " ".join(output)




