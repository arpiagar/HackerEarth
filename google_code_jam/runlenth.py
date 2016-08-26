
#25626 25757 24367 24267 16 100 2 7277

input_list = raw_input().split(" ")
input_list = [int(x) for x in input_list]


def runlength(input_list):
  new_list = []
  if len(input_list) > 0:
    new_list.append(input_list[0])
    prev = input_list[0]
  else:
    return new_list

  for i in xrange(1,len(input_list)):
    new_elem = input_list[i] - prev
    if new_elem > 127 or new_elem < -127:
      new_list.append(-128)
    prev = input_list[i]
    new_list.append(new_elem)
  return new_list

 

output_list = runlength(input_list)
output_list = [str(x) for x in output_list]
print " ".join(output_list)