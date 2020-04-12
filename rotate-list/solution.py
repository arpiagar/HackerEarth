https://leetcode.com/problems/rotate-list/submissions/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        count = 0
        elem = head
        while(elem != None):
            count += 1
            elem = elem.next
        number = count - (k % count)
        if count == number:
            return head
        elem = head
        count = 1
        while count < number:
            count += 1
            elem = elem.next
        temp = head
        head = elem.next
        elem.next = None
        elem = head
        while elem.next != None:
             elem = elem.next
        elem.next = temp
        return head

