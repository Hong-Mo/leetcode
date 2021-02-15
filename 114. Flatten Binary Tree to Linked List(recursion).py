# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, node, order):
        order.append(node)
        
        if node.left:
            self.preorder(node.left, order)
        
        if node.right:
            self.preorder(node.right, order)
        
        
    def flatten(self, root: TreeNode) -> None:
        order = []
        
        if root:
            self.preorder(root, order)

            for i in range(len(order)-1):
                order[i].left = None
                order[i].right = order[i+1]

            order[-1].left = order[-1].right = None