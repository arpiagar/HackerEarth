arr1 = [1, 4, 2, 6, 1, 4, 6, 7, 6, 4]
arr2 = [1, 4, 2, 6, 1, 4, 6, 7, 6]
k = 2
# [6, 4]
#
#Sort by freq
def topKelements(arr, k):
    """ Find the top k elements in the order of their frequency"""
    frequency_map={} #
    for elem in arr: # o(N)
        if elem in frequency_map:
            frequency_map[elem] += 1
        else:
            frequency_map[elem] = 1 # {1:2,4:3,6:3,7:1}
    temp_list =  [(k,v) for k,v in frequency_map.items()] #[(1,2),(4,3)...]
    temp_list= sorted(temp_list, key = lambda x: x[1], reverse=True) # ON(log(N))#[(4,3),(6,3)]
    out_list = []
    n = len(temp_list)
    count = 0
    for i in range(k): # O(N)
        out_list.append(temp_list[i][0]) #(4,3), 4-id

    last_frequency = temp_list[k-1][1]
    for i in range(k, len(temp_list)): #O
        elem = temp_list[i]
        if elem[1] == last_frequency:
            out_list.append(elem[0])
        else:
            break
    return out_list
[1, 4, 2, 6, 1, 4, 6, 7, 6, 4]

(freq, id) (freq,id2)
{id => obj)

res1 = topKelements(arr1, k)
res2 = topKelements([1], k)
print(res1)
print(res2)
