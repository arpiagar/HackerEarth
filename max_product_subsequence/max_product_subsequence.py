# def max_product(input_str):
#   product = 1
#   max_product = 1
#   start_idx = 0
#   i =  start_idx
#   while i < len(input_str):
#     if input_str[i] != 0:
#       product = product * input_str[i]
#       if product > max_product:
#         max_product = product
#         max_start = start
#         max_end = i 
#     else:
#       j = max_end
#       while j>=0 :
#         if input_str[j] < 0:
#           j -= 1
#         else:
#           break
#     temp_product = 1
#     for i in xrange(start_idx,j+1):
#       temp_product = temp_product * i 
#     if temp_product > max_product:
#       max_product = temp_product


	

def find_first_negative(input_str):
  for i  in xrange(0,len(input_str)):
    if input_str[i] <0:
      return i

def find_last_negative(input_str):
  for i  in xrange(len(input_str)-1,-1,-1):
    if input_str[i] <0:
      return i

def max_pr(input_str):
  product = 1
  for elem in input_str:
    product = elem * product

  if product < 0:
    start = find_first_negative(input_str)
    end = find_last_negative(input_str)
    start_product =  1
    end_product = 1
    for i in xrange(0,start+1):
      start_product = start_product* input_str[i]
    for i in xrange(len(input_str)-1,end,-1):
      end_product = end_product* input_str[i]
    return max(product/start_product,product/end_product,start_product/input_str[start],end_product/input_str[end])
  return product

if __name__ == "__main__":
  input_list = [2,4,-7,2,-5,-6,3,13]
  print max_pr(input_list)
