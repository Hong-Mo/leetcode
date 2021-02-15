# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursion(self, pre, cur):
        if not cur:
            return pre
        
        store = cur.next
        cur.next = pre
        pre, cur = cur, store
        
        return self.recursion(pre, cur)
        
    
    def reverseList(self, head: ListNode) -> ListNode:
        return self.recursion(None, head)