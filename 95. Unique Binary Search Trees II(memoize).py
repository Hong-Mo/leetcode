# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self, start, end, dic):
        if start==end:
            return [TreeNode(start)]
      
        elif start>end:
            return [None]
        
        ins  = []
        
        for i in range(start, end+1):
            if (start, i-1) not in dic.keys():
                left = self.recursive(start, i-1, dic)
                dic[(start, i-1)] = left
            
            else:
                left = dic[(start, i-1)]
            
            if (i+1, end) not in dic.keys():
                right = self.recursive(i+1, end, dic)
                dic[(i+1, end)] = right
            
            else:
                right = dic[(i+1, end)]
            
            for l_node in left:
                for r_node in right:
                    root = TreeNode(i)
                    root.left, root.right = l_node, r_node
                    ins.append(root)
        
        return ins
    
    def generateTrees(self, n: int) -> List[TreeNode]:
        dic = {}
        
        if n<1:
            return []
        
        return self.recursive(1, n, dic)