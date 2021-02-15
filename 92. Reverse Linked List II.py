# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        con_front, pre, cur = None, None, head
        count = 1
        
        while count<=n:
            if count>m:
                store = cur.next
                cur.next = pre
                pre, cur = cur, store

            else:
                if count==m:
                    con_front = pre
                    con_tail = cur
                    
                pre, cur = cur, cur.next
                
            count += 1
        
        con_tail.next = cur
        
        if not con_front:
            return pre
        
        con_front.next = pre
        
        return head