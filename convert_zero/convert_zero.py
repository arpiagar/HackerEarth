

def find_index(input_array):
  i = 0
  j = 0
  flag = True
  index_array = []
  for index,elem in enumerate(input_array):
    if elem == 0:
      index_array.append(index)

  #import pdb;pdb.set_trace()
  max_diff = 0
  start = 0
  end = len(input_array)-1
  prev  = start
  max_val = 0
  ret_index = 0
  for index, elem in enumerate(index_array):
      start_diff  = elem - start
      if elem  < len(input_array)-2:
        end_diff =  index_array[index+1] - elem
      else:
        import pdb;pdb.set_trace()
        end_diff = end - index_array[index] 
      val =  end_diff+start_diff+1
      if val > max_val:
        max_val = val
        ret_index =  elem
  return ret_index





if __name__ == "__main__":
  input_array = [1,1,0,1,1,1,1,0,0,1,1,0,1,1,1,1,1,1]
  k =  [2, 7, 8, 11]
  print find_index(input_array)
