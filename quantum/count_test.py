

def print_counts(first_array, second_array):
    out_array = []
    for element in second_array:
        less_than_array = [ x for x in first_array if x <= element]
        out_array.append(len(less_than_array))
    print(out_array)



if __name__ == "__main__":
    n = 4
    nums =  [1,4,2,4]
    m = 2
    maxes = [3, 5]
    print_counts(nums, maxes)
