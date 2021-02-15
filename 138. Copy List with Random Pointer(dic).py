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
            dic = {None:None}
            copy_head = copy_cur = Node(head.val)
            dic[head] = copy_head
            cur = head.next
            
            while cur:
                copy_cur.next = Node(cur.val)
                copy_cur = copy_cur.next
                dic[cur] = copy_cur
                cur = cur.next
                
            cur, copy_cur = head, copy_head
            
            while cur:
                copy_cur.random = dic[cur.random]
                cur, copy_cur = cur.next, copy_cur.next
                
            return copy_head
        
        return None