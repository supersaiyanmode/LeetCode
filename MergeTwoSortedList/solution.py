# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = None
        head = None
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                if res is None:
                    res = l1
                    head = l1
                else:
                    res.next = l1
                    res = res.next
                l1 = l1.next
            else:
                if res is None:
                    res = l2
                    head = l2
                else:
                    res.next = l2
                    res = res.next
                l2 = l2.next
        while l1 is not None:
            if res is None:
                res = l1
                head = l1
            else:
                res.next = l1
                res = res.next
            l1 = l1.next
        while l2 is not None:
            if res is None:
                res = l2
                head = l2
            else:
                res.next = l2
                res = res.next
            l2 = l2.next
        return head