# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Hardware Limit (Null Pointer):
        if not root:
            return False
        
        # State Mutation (Pre-Order):
        targetSum = targetSum - root.val

        # Leaf Node Audit (The Success Gate):
        if not root.left and not root.right:
            return targetSum == 0
        
        # The Logic Or (Short-Circuit Evaluation)
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)