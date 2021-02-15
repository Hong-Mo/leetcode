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
        level = [root]
        
        while level[0]:
            ins = []
            
            level.append(None)
            
            for i in range(0, len(level)-1):
                level[i].next = level[i+1]
                ins.append(level[i].left)
                ins.append(level[i].right)
            
            level[:] = ins
        
        return root