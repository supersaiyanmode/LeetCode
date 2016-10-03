# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = sorted([x for x in lists if x is not None], key=lambda x: x.val)
        if not lists:
            return []
        
        res = None
        head = None
        while lists:
            cur = lists[0]
            lists[0] = lists[0].next
            if lists[0] is None:
                del lists[0]
            elif len(lists) > 1:
                i = 1
                while i < len(lists) and lists[i].val < lists[i-1].val:
                    lists[i-1], lists[i] = lists[i], lists[i-1]
                    i += 1
            if res is None:
                res = cur
                head = cur
            else:
                res.next = cur
                res = cur
        return head
                    
                    