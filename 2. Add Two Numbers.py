# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = head = ListNode()
        carry  = 0
        
        while l1 and l2:
            l3.next = ListNode()
            l3 = l3.next
            
            s = l1.val + l2.val + carry
            l3.val = s%10
            carry = s//10
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            l3.next = ListNode()
            l3 = l3.next
            
            s = l1.val  + carry
            l3.val = s%10
            carry = s//10
            l1 = l1.next
        
        while l2:
            l3.next = ListNode()
            l3 = l3.next
            
            s = l2.val  + carry
            l3.val = s%10
            carry = s//10
            l2 = l2.next
        
        if carry :
            l3.next = ListNode(1)
        
        return head.next