i#https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/submissions/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        q = [head] # 1
        while q :
            temp = q.pop(0) # 3
            if temp and temp.child: #
                if temp.next:
                    q.insert(0,temp.next) # [4]
                temp.next = temp.child
                temp.next.prev = temp
                temp.child = None#7
                q.insert(0,temp.next)#[8,4]
            else:
                prev = None
                while temp and temp.child == None: # 3
                    prev = temp
                    temp = temp.next
                if temp:
                    q.insert(0,temp) #
                else:
                    if q:
                        prev.next = q[0]
                        q[0].prev = prev
        # temp = head
        # while temp:
        #     print(temp.val, temp.next and temp.next.val, temp.prev and temp.prev.val)
        #     temp = temp.next
        return head
