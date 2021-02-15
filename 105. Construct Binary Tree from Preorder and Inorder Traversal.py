# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        
        root_val, root_i = preorder[0], inorder.index(preorder[0])
        root = TreeNode(root_val)
        
        root.left = self.buildTree(preorder[1:1+root_i], inorder[:root_i])
        root.right = self.buildTree(preorder[1+root_i:], inorder[root_i+1:])
        
        return root