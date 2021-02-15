"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        level = []
        
        if root:
            level.append(root)
        
        while level:
            ins = []
            
            level.append(None)
            
            for i in range(0, len(level)-1):
                level[i].next = level[i+1]
                
                if level[i].left:
                    ins.append(level[i].left)
                
                if level[i].right:
                    ins.append(level[i].right)
            
            level[:] = ins
        
        return root