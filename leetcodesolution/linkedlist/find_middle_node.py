class Solution:
    def __init__(self, head):
        self.head = head
        self.next = None



def find_middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


head = Solution(1)
head.next = Solution(2)
head.next.next = Solution(3)
head.next.next.next = Solution(4)
head.next.next.next.next = Solution(5)

# Find and print the middle node
middle_node = find_middle_node(head)
print(middle_node.head)

