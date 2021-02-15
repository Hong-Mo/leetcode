# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, node, l_bound, u_bound):
        if not node:
            return True
        
        if node.val<=l_bound or node.val>=u_bound:
            return False
        
        return (self.check(node.left, l_bound, min(node.val, u_bound)) 
                and self.check(node.right, max(l_bound, node.val), u_bound))
        
    def isValidBST(self, root: TreeNode) -> bool:
        
        return self.check(root, float('-inf'), float('inf'))