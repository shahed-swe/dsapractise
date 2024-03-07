import heapq


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ListNode.__lt__ = lambda self, other: self.val < other.val

        min_heap = []

        for l in lists:
            if l:
                heapq.heappush(min_heap, l)

        temp = ListNode(0)
        current = temp

        while min_heap:
            node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, node.next)
        return temp.next
