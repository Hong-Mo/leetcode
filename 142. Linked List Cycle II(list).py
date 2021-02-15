# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node = []
        cur = head
        
        while cur:
            if cur in node:
                return cur
            
            node.append(cur)
            cur = cur.next
        
        return cur