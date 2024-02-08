# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        items = set()
        while head and head.next is not None:
            if head in items:
                return True
            else:
                items.add(head)
                head = head.next
        return False
        