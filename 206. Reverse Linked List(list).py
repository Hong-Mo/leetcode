# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        store = []
        
        while cur:
            store.append(cur)
            cur = cur.next
        
        for i in range(len(store)-1, 0, -1):
            store[i].next = store[i-1]
        
        if store:
            store[0].next = None
            head = store[-1]
        
        return head