# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue, ans = [], []
        
        if root:
            queue.append((root, 0))
        
        while queue:
            node, level = queue.pop(0)
            
            try:
                ans[level].append(node.val)
            
            except:
                ans.append([node.val])
            
            if node.left:
                queue.append((node.left, level+1))
            
            if node.right:
                queue.append((node.right, level+1))
        
        cur = 1
        
        while cur<len(ans):
            ans[cur].reverse()
            cur += 2
        
        return ans