"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head:
            copy_head = copy_cur = Node(head.val)
            cur = head.next
            
            while cur:
                copy_cur.next = Node(cur.val)
                cur, copy_cur = cur.next, copy_cur.next
            
            cur, copy_cur = head, copy_head
            
            while copy_cur:
                search, search_copy = head, copy_head
                
                while search!=cur.random:
                    search = search.next
                    search_copy = search_copy.next
                
                copy_cur.random = search_copy
                cur, copy_cur = cur.next, copy_cur.next
        
            return copy_head
        
        return None