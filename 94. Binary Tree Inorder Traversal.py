# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def visit(self, node, ans):
        if node.left:
            self.visit(node.left, ans)
            
        ans.append(node.val)
        
        if node.right:
            self.visit(node.right, ans)
            
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        
        if root:
            self.visit(root, ans)
        
        return ans