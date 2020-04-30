# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = -math.inf
    
    def func(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = max(self.func(root.left), 0)
        right = max(self.func(root.right), 0)
        self.ans = max(self.ans, left + right + root.val)
        return root.val + max(left, right)
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.func( root)
        return self.ans
