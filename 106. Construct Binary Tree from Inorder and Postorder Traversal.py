# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        
        root_val, root_i = postorder[-1], inorder.index(postorder[-1])
        root = TreeNode(root_val)
        
        root.left = self.buildTree(inorder[:root_i], postorder[:root_i])
        root.right = self.buildTree(inorder[root_i+1:], postorder[root_i:-1])
        
        return root