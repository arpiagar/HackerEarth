# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        p1 = l1
        p2 = l2
        head = None
        flag = False
        prev = None
        carry = 0
        while(p1!= None and p2 != None):

                num = p1.val+ p2.val + carry
                carry = 0
                if num >= 10:
                    carry = num/10
                    num = num % 10
                p3 =  ListNode(num)
                if prev != None:
                    prev.next = p3
                if not flag:
                    head = p3
                    flag =  True
                p1 = p1.next
                p2 = p2.next
                prev = p3
        while( p1 != None):
            num  = p1.val + carry
            carry = 0
            if num >= 10:
                carry = num/10
                num = num % 10
            p3 =  ListNode(num)
            if prev != None:
                prev.next = p3
            prev = p3
            if not flag:
                head = p3
                flag = True
            p1 = p1.next
        while(p2 != None):
            num  = p2.val + carry
            carry = 0
            if num >= 10:
                carry = num/10
                num = num % 10
            p3 =  ListNode(num)
            if prev != None:
                prev.next = p3
            prev = p3
            if not flag:
                head = p3
                flag = True
            p2 = p2.next
        if carry:
            prev.next = ListNode(carry)
        return head


        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

