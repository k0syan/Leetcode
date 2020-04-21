# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstHelper(order: List[int], s: int, e: int) -> TreeNode: 
        if s == e:
            return
        lo, hi = s + 1, e - 1
        while lo <= hi:
            mi = lo + (hi - lo) // 2
            if order[s] > order[mi]:
                lo = mi + 1
            else:
                hi = mi - 1
        root = TreeNode(order[s])
        root.left = Solution.bstHelper(order, s + 1, lo)
        root.right = Solution.bstHelper(order, lo, e)
        return root
    
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return Solution.bstHelper(preorder, 0, len(preorder))
        
