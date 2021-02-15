# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:       
    def mergesort(self, head, l):
        if l==1:
            head.next = None
            return head
        
        half = count = l//2
        another_head = head
        
        while count>0:
            another_head = another_head.next
            count -= 1
        
        head, li, another_li = ListNode(0), self.mergesort(head, half), self.mergesort(another_head, l-half)
        tail = head
            
        while li and another_li:
            if li.val<another_li.val:
                tail.next = li
                li = li.next
            
            else:
                tail.next = another_li
                another_li = another_li.next
            
            tail = tail.next
            
        if li:
            tail.next = li
        
        else:
            tail.next = another_li
        
        return head.next
    
    def sortList(self, head: ListNode) -> ListNode:
        cur = head
        l = 0
        
        while cur:
            cur=cur.next
            l += 1
        
        if head:
            head = self.mergesort(head, l)
        
        return head