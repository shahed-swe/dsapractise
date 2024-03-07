# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = ListNode(0)
        temp.next = head
        slow = temp
        fast = temp

        for _ in range(n + 1):
            slow = slow.next

        while slow is not None:
            slow = slow.next
            fast = fast.next

        fast.next = fast.next.next
        return temp.next
