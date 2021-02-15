# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head and head.next!=None:
            p = head
            count = 0
            
            while p!=None:
                p = p.next
                count += 1
            
            k %= count
            
            while k!=0:
                pre = head

                while (pre.next).next!=None:
                    pre = pre.next
                
                tail = pre.next
                pre.next = None
                tail.next = head
                head = tail
                k -= 1
        
        return head