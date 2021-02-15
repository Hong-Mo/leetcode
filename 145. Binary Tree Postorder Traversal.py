# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        order, ans = [], []
        
        if root:
            order.append(root)
        
        while order:
            cur = order[0]
            
            if cur.right:
                order.insert(0, cur.right)
            
            if cur.left:
                order.insert(0, cur.left)
            
            if not cur.left and not cur.right:
                ans.append(cur.val)
                del order[0]
            
            cur.left = cur.right = None
        
        return ans