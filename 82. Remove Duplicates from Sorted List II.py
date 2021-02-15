# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        pre = head = None
        
        while cur:
            duplicate = 0
            
            if (not cur.next) or cur.val!=(cur.next).val:
                duplicate = 1
            
            else:
                while cur.next and cur.val==(cur.next).val:
                    cur = cur.next
                    
            if duplicate:
                if (not pre):
                    head = cur
                
                pre = cur
            
            elif pre:
                pre.next = cur.next
            
            cur = cur.next
        
        return head