#https://leetcode.com/problems/middle-of-the-linked-list/solution/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return head
        temp = head
        length = 0
        while(temp):
            temp = temp.next
            length += 1
        mid = length//2
        temp = head
        while(mid):
            temp = temp.next
            mid -= 1
        return temp
