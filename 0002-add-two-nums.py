# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        res = ListNode()
        head = res
        while l2 is not None and l1 is not None:
            total = l1.val + l2.val + carry
            if total > 9:
                carry = 1
                res.val = total % 10
            else:
                carry = 0
                res.val = total
            l1 = l1.next
            l2 = l2.next
            if l1 is not None and l2 is not None:
                res.next = ListNode()
                res = res.next

        if l2 is not None:
            rest = l2
        elif l1 is not None:
            rest = l1
        else:
            if carry == 1:
                res.next = ListNode()
                res = res.next
                res.val = 1
            return head
        
        res.next = ListNode()
        res = res.next
        
        while rest is not None:
            total = rest.val + carry
            if total > 9:
                carry = 1
                res.val = total % 10
            else:
                carry = 0
                res.val = total
            rest = rest.next
            if rest is not None:
                res.next = ListNode()
                res = res.next
        if carry == 1:
            res.next = ListNode()
            res = res.next
            res.val = 1
        return head
            
sol = Solution()
k = ListNode(9, None)
j = ListNode(9, k)
i = ListNode(9, j)
h = ListNode(9, i)
g = ListNode(9, None)
f = ListNode(9, g)
e = ListNode(9, f)
d = ListNode(9, e)
c = ListNode(9, d)
b = ListNode(9, c)
a = ListNode(9, b)
print(sol.addTwoNumbers(a, d))