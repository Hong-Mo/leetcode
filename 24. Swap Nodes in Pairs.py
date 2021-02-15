# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p = head
        count = 0
        
        while p!=None:
            p = p.next
            count += 1
        
        if count>1:
            pre, cur, nex = head, head.next, (head.next).next
            head = cur

            for i in range((count//2)-1):
                pre.next = nex.next
                cur.next = pre

                cur = nex.next
                pre = nex
                nex = cur.next

            cur.next = pre
            pre.next = nex
        
        return head