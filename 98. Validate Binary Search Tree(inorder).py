# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def visit(self, node, pre):
        if node.left and not self.visit(node.left, pre):
            return False
        
        if node.val>pre[0]:
            pre[0] = node.val
        
        else:
            return False
        
        if node.right and not self.visit(node.right, pre):
            return False
        
        return True
        
    def isValidBST(self, root: TreeNode) -> bool:
        if root:
            return self.visit(root, [float('-inf')])
        
        return True