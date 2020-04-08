# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        l = head
        n = 0
        while l != None:
            n += 1
            l = l.next
        for i in range(n // 2):
            head = head.next
        return head
            
