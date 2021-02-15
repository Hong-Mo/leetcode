# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        p = head
        
        while p!=None:
            p = p.next
            count += 1
            
        move = count-n
        pre, p = None, head
        
        while move>0:
            pre = p
            p = p.next
            move -= 1
        
        if pre==None:
            head = p.next
                
        else:
            pre.next = p.next
        
        return head