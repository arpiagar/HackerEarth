def sort_array(orig_array, index_array):
    count = 0
    max_count = len(index_array)
    curr_idx = 0
    temp = -1
    while count < max_count:
        required_idx =  index_array[curr_idx]
        if temp != -1:
            curr_value = temp
        else:
            curr_value = orig_array[curr_idx]
        temp = orig_array[required_idx]
        orig_array[required_idx] =  curr_value
        count += 1
        curr_idx = required_idx
    print orig_array

sort_array(["C","D","E","F","G"], [3,0,4,1,2])

#[C,D,E,F,G]

#[3,0,4,1,2]

#[D,F,G,C,E]
