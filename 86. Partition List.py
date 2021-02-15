# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_pre = more_head = more_pre = None
        cur = head
        
        while cur:
            if cur.val<x:
                if not less_pre:
                    less_pre = head = cur
                
                else:
                    less_pre.next = cur
                    less_pre = cur
            
            else:
                if not more_head:
                    more_head = more_pre = cur
                    
                else:
                    more_pre.next = cur
                    more_pre = cur
            
            cur = cur.next
        
        if not less_pre:
            head = more_head
        
        else:
            less_pre.next = more_head
            
            if more_pre:
                more_pre.next = None
        
        return head