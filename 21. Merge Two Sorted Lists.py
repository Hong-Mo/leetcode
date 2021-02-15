# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l3 = ListNode()
        head = l3
        
        while l1 and l2 :
            
            l3.next = ListNode()
            l3 = l3.next
            
            if l1.val > l2.val:
                l3.val = l2.val
                l2 = l2.next
            
            else:
                l3.val = l1.val
                l1 = l1.next
            
        
        while l1 :
            l3.next = ListNode()
            l3 = l3.next
            
            l3.val = l1.val
            l1 = l1.next
            
        
        while l2 :
            l3.next = ListNode()
            l3 = l3.next
            
            l3.val = l2.val
            l2 = l2.next
            
            
        
        return head.next