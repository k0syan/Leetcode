# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        c = head
        if head is not None:
            n = head.next
        else:
            return
        while n is not None:
            if c.val != n.val:
                c.next = n
                c = c.next
            else:
                c.next = None
            n = n.next
        return head
