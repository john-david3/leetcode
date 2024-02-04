# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head:
            while head.next and head.next.val == head.val:
                head.next = head.next.next
            if head.next:
                self.deleteDuplicates(head.next)
            return head
        else:
            return None
    
e = ListNode(3, None)
d = ListNode(3, e)
c = ListNode(2, d)
b = ListNode(1, c)
a = ListNode(1, b)

sol = Solution()
sol.deleteDuplicates(a)