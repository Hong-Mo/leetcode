# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        stk = []
        
        if root:
            stk.append(None)
            node = root
        
        while stk:
            while node:
                if node.right:
                    stk.append(node.right)
                
                if not node.left:
                    break
                
                node.left, node.right = None, node.left
                node = node.right

            node.right = stk.pop()
            node = node.right