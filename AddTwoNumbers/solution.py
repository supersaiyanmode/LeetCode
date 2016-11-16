# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return ListNode(carry) if carry else None
        if l1 and not l2:
            value = l1.val + carry
            l1.val = value % 10
            l1.next = self.addTwoNumbers(l1.next, None, value/10)
            return l1
        if not l1 and l2:
            value = l2.val + carry
            l2.val = value % 10
            l2.next = self.addTwoNumbers(None, l2.next, value/10)
            return l2
        value = l1.val + l2.val + carry
        ret = ListNode(value%10)
        ret.next = self.addTwoNumbers(l1.next, l2.next, value/10)
        return ret