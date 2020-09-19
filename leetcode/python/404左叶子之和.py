# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0
        def dfs(node):
            
            if not node:
                return 0
            elif node.left and not node.left.left and not node.left.right:
                self.sum += node.left.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.sum