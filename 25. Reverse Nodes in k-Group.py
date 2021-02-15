# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count, cur = 0, head
        
        while cur!=None:
            count, cur = count+1, cur.next
        
        if count>=k:
            pre_tail, pre, cur, head = None, None, head, None
        
        while count>=k:
            tail, move = cur, 0
            
            while move<k:
                store = cur.next
                cur.next = pre
                pre, cur = cur, store
                move += 1

            if not head:
                head = pre
            
            if pre_tail:
                pre_tail.next = pre
                
            pre, pre_tail, count = None, tail, count-k
        
        tail.next = cur
        
        return head