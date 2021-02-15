# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root :
            return False
        
        target = sum-root.val
        
        if (not root.left and not root.right) and target==0:
            return True
        
        elif ((root.left and self.hasPathSum(root.left, target)) or
             (root.right and self.hasPathSum(root.right, target))):   
            return True
        
        return False