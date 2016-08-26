"abcdefedcsddnjd"

def find_longest_palindrome(input_string):
  n =  len(input_string)
  max_length = 0
  start_index = -1
  end_index = -1
  if n == 1: # Just in case the string length is of length 1
    return input_string
  for i in xrange(0,n-1):
    if input_string[i] == input_string[i+1]:
      temp_start_index =  i
      j = i
