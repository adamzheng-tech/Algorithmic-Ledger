# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
        
            left_depth = dfs(node.left)
            if left_depth == -1:
                return -1

            right_depth = dfs(node.right)
            if right_depth == -1:
                return -1
        
            if abs(left_depth - right_depth) > 1:
                return -1
        
            return max(left_depth, right_depth) + 1

        return dfs(root) != -1    