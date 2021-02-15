# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def path(self, node, num, ans):
        num += node.val
        
        if not node.left and not node.right:
            ans[0] += num
        
        if node.left:
            self.path(node.left, num*10, ans)
        
        if node.right:
            self.path(node.right, num*10, ans)
            
    def sumNumbers(self, root: TreeNode) -> int:
        ans = [0]
        
        if root:
            self.path(root, 0, ans)
        
        return ans[0]