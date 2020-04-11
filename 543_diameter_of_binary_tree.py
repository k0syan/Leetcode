# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    diameter = 0
    
    def depth(root: TreeNode):
        if root == None:
            return 0
        left = Solution.depth(root.left)
        right = Solution.depth(root.right)
        Solution.diameter = max(Solution.diameter, left + right)
        return 1 + max(left, right)
        
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        Solution.diameter = 0
        Solution.depth(root)
        return Solution.diameter
