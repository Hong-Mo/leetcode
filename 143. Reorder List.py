# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head:
            li = []
            cur = head

            while cur:
                li.append(cur)
                cur = cur.next

            cur, i = li.pop(0), 1

            while li:
                if i%2==0:
                    node = li.pop(0)

                else:
                    node = li.pop(-1)

                cur.next = node
                cur = node
                i += 1

            cur.next = None