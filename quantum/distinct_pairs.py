def find_pairs(input_array, target):
    s = set([])
    temp_map = {}
    for elem in input_array:
        key = target-elem
        if key in temp_map:
            temp_map[key] += 1
        else:
            temp_map[key] = 1
    # Ensure that if half of the target is present, it has 2 occurrence.
    if target%2 ==0:
        mid = target/2
        if mid in temp_map and temp_map[mid] == 1:
            temp.pop(mid)
    for elem in input_array:
        if elem in temp_map:
            arr =  [elem, target-elem]
            arr.sort()
            s.add(tuple(arr))
    import pdb;pdb.set_trace()
    return len(dict(s).keys())








if __name__ == "__main__":
    n = int(input())
    input_array = []
    for i in range(n):
        input_array.append(int(input()))
    final_number =  int(input())
    find_pairs(input_array, final_number)
