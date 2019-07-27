
def add_to_hash(special_map, string, index):
    if index == 0:
        for elem in string:
            if not special_map.has_key(elem):
                special_map[elem] = index
        return special_map
    else:
        new_map = {}
        for elem in string:
            if special_map.has_key(elem):
                new_map[elem] = index
        return new_map


if __name__ == "__main__":
    n = int(raw_input())
    for i in xrange(0, n):
        special_map = {}
        j = int(raw_input())
        for k in xrange(0, j):
            s = raw_input()
            special_map = add_to_hash(special_map, s,k)
        print len(special_map.keys())

