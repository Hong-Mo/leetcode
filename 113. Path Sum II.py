# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findPath(self, node, cur, sum, ans):
        target = sum-node.val
        cur.append(node.val)
        
        if (not node.left and not node.right) and target==0:
            ans.append(cur)
        
        if node.left:
            self.findPath(node.left, cur[:], target, ans)
        
        if node.right:
            self.findPath(node.right, cur[:], target, ans)
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        
        if root:
            self.findPath(root, [], sum, ans)
        
        return ans