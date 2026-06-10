# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # The initialization audit.
        if not root:
            return True
        
        def isMirror(p_a, p_b):
            # Hardware Limits (The Base Cases).
            if p_a == p_b == None:
                return True
            elif p_a == None and p_b != None:
                return False
            elif p_b == None and p_a != None:
                return False
            # The Payload Audit. 
            elif p_a.val != p_b.val:
                return False
            # The Synchronized Recursive Split.
            else:
                return isMirror(p_a.left, p_b.right) and isMirror(p_b.left, p_a.right)
        
        return isMirror(root.left, root.right)
                  