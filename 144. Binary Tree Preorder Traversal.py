# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        order, ans = [], []
        
        if root:
            order.append(root)
        
        while order:
            cur = order.pop(0)
            ans.append(cur.val)
            
            if cur.right:
                order.insert(0, cur.right)
            
            if cur.left:
                order.insert(0, cur.left)
        
        return ans