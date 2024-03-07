# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if (head is None) or (k == 1):
            return head

        def reverse_linked_list(start, end):
            prev, curr = None, start
            while curr != end:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev

        temp = ListNode(0)
        temp.next = head
        group_prev = temp

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return temp.next

            group_next = kth.next
            new_group_head = reverse_linked_list(group_prev.next, group_next)

            temp2 = group_prev.next
            group_prev.next = new_group_head
            temp2.next = group_next

            group_prev = temp2
