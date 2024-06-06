# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        check_list = []
        while head:
            check_list.append(head.val)
            head = head.next
        return check_list == list(reversed(check_list))