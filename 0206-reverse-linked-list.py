# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head.next.next is not None:
            self.reverseList(head.next)
        head.next.next = head
        return head

e = ListNode(5, None)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)
s = Solution()
s.reverseList(a)