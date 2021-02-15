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
    def recursion(self, node):
        (node.left).next = node.right
        
        if node.next:
            (node.right).next = (node.next).left
        
        if node.left.left:
            self.recursion(node.left)
            self.recursion(node.right)
        
    def connect(self, root: 'Node') -> 'Node':
        if root and root.left:
            self.recursion(root)
        
        return root