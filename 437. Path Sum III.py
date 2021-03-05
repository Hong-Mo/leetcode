# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def toleaf(self, node, path, sum):
        if not node:
            return 0
        
        ans = 0
        path.append(0)
        
        for i in range(len(path)):
            path[i] += node.val
            
            if path[i]==sum:
                ans += 1
                
        return ans+self.toleaf(node.left, path[:], sum)+self.toleaf(node.right, path[:], sum)
        
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.toleaf(root, [], sum)