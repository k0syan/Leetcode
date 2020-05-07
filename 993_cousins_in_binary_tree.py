# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        res = {}
        def helper(root, d = 0, par = None):
            if root:
                if root.val in (x, y): res[root.val] = (d, par)
                helper(root.left, d = d + 1, par = root.val)
                helper(root.right, d = d + 1, par = root.val)
        helper(root)
        return res[x][0] == res[y][0] and res[x][1] != res[y][1]
        
