# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        newHead = ListNode(-1)
        newHead.next = head
        head = newHead
        while head.next != None:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return newHead.next
