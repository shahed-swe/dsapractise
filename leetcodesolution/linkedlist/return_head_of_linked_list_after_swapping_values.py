# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        slow = head
        fast = head

        kth_from_start = None
        for _ in range(k - 1):
            slow = slow.next
        kth_from_start = slow

        while slow.next:
            slow = slow.next
            fast = fast.next

        kth_from_start.val, fast.val = fast.val, kth_from_start.val

        return head
