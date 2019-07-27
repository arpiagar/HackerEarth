#You have an unsorted array, and you are given a value S. Find all pairs of elements in the array that add up to value S.

def two_sum(array, target_sum):
    elem_hash = {}
    for elem in array:
        elem_hash[elem] = 1

    out = []
    for elem in array:
        new_elem =  target_sum - elem
        if elem_hash[new_elem]:
            out.append((elem, new_elem))
            elem_hash[elem] = 0
            elem_hash[new_elem] = 0
    return out

