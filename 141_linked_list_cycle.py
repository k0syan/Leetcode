# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        sl = fa = head
        while sl != None:
            sl = sl.next
            if fa == None or fa.next == None:
                return False
            fa = fa.next
            fa = fa.next
            if fa == sl:
                return True
        return False
