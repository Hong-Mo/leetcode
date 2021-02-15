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
    def recursive(self, node):
        if node.right:
            if node.left:
                (node.left).next = node.right
            
            next_node = node.next
            
            while next_node:
                if next_node.left:
                    (node.right).next = next_node.left
                    break
                
                elif next_node.right:
                    (node.right).next = next_node.right
                    break
                
                next_node = next_node.next
        
        elif node.left:
            next_node = node.next
            
            while next_node:
                if next_node.left:
                    (node.left).next = next_node.left
                    break
                
                elif next_node.right:
                    (node.left).next = next_node.right
                    break
                
                next_node = next_node.next
        
        if node.right:
            self.recursive(node.right)
            
        if node.left:
            self.recursive(node.left)
        
    def connect(self, root: 'Node') -> 'Node':
        if root:
            self.recursive(root)
        
        return root