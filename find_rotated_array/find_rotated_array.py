def find_rotated_array(input_string, element, start, end):
    mid =  (start+end)/2
    if element == input_string[start]:
        return start
    if element == input_string[end]:
        return end
    if element == input_string[mid]:
        return mid
    if start < end:
        if element > input_string[start] and element < input_string[mid]:
            end  = mid-1
            return find_rotated_array(input_string, element, start, end)
        elif element > input_string[start] and element > input_string[mid]:
            end  = mid-1
            return find_rotated_array(input_string, element, start, end)
        else:
            start =  mid + 1
            return find_rotated_array(input_string, element, start, end)
  


input_string = [6,7,8,9,10,11,1,2,3,4,5]

print find_rotated_array(input_string, 3, 0, len(input_string)-1)
print find_rotated_array(input_string, 7, 0, len(input_string)-1)
