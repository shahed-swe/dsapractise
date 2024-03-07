# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = ListNode(0)
        temp.next = head
        current = temp

        while current.next and current.next.next:
            slow = current.next
            fast = current.next.next

            slow.next = fast.next
            fast.next = slow
            current.next = fast

            current = slow

        return temp.next
