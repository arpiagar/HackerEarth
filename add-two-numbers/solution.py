#https://leetcode.com/problems/add-two-numbers/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def form_carry_from_val(self, v):
        if v >= 10:
            carry = 1
            v = v % 10
        else:
            carry = 0
        return v,carry
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        if p1 and not p2:
            return p1
        if p2 and not p1:
            return p2
        head = None
        temp = None
        carry = 0
        while(p1 and p2):
            v = p1.val + p2.val + carry
            v, carry = self.form_carry_from_val(v)
            node =  ListNode(v)
            if not head:
                head = node
                temp = head
            else:
                temp.next = node
                temp = node
            p1 = p1.next
            p2 = p2.next
        if p1:
            while(p1):
                v = p1.val + carry
                v, carry = self.form_carry_from_val(v)
                print("ppi1",v,carry)
                node =  ListNode(v)
                temp.next = node
                temp = node
                p1 = p1.next
        if p2:
            while(p2):
                v = p2.val + carry
                v, carry = self.form_carry_from_val(v)
                print("ppi2",v,carry)
                node =  ListNode(v)
                temp.next = node
                temp = node
                p2 = p2.next
        if carry:
            temp.next = ListNode(carry)
        return head
