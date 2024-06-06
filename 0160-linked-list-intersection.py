# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        listA = set()
        while headA:
            listA.add(headA)
            headA = headA.next
        while headB:
            if headB in listA:
                return headB
            else:
                headB = headB.next
        return None