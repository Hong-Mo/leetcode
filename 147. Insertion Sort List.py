# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head and head.next:
            pre, cur = head, head.next
            
            while cur:
                pre_comp, comp = None, head
                
                while comp and comp.val<cur.val:
                    pre_comp = comp
                    comp = comp.next
                    
                if comp==cur:
                    pre = cur
                
                else:
                    if pre_comp:
                        pre_comp.next = cur
                        
                    else:
                        head = cur
                        
                    pre.next = cur.next
                    cur.next = comp
                    
                cur = pre.next
            
        return head