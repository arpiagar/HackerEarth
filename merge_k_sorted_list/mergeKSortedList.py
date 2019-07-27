# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def get_next_element(lists, input_map, index=None):
    if index == None:
        for i in xrange(0, len(lists)):
            sub_list = lists[i]
            if sub_list and sub_list.val != None:
                if input_map.has_key(sub_list.val):
                    input_map[sub_list.val].append(i)
                else:
                    input_map[sub_list.val] = [i]
            else:
                continue
            lists[i] = lists[i].next
    else:
        sub_list = lists[index]
        if sub_list and sub_list.val != None:
            if input_map.has_key(sub_list.val):
                input_map[sub_list.val].append(index)
            else:
                input_map[sub_list.val] = [index]

            lists[index] = lists[index].next
    if len(input_map.keys()) > 0:
        min_val = min(input_map.keys())
    else:
        return -1,-1,{}
    if len(input_map[min_val]) > 1:
        print input_map[min_val]
        first_idx = input_map[min_val][0]
        input_map[min_val] = input_map[min_val][1:]
    else:
        first_idx = input_map.pop(min_val)[0]
    return min_val, first_idx, input_map

class Solution(object):
    def mergeKLists(self, lists):
        ret_map = {}
        idx = None
        out = []
        while True:
            min_val, idx, ret_map = get_next_element(lists, ret_map, idx)
            if idx == -1:
                break
            else:
                out.append(min_val)
        return out
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

