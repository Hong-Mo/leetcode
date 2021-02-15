# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min_heap = []
        corres = defaultdict(list)
        head, min_num = None, 10001
        
        for node in lists:
            if node:
                heapq.heappush(min_heap, node.val)
                corres[node.val].append(node)

        while min_heap:
            node = corres[heapq.heappop(min_heap)].pop(0)
            
            if not head:
                head = cur = node
            
            else:
                cur.next = node
                cur = cur.next
            
            if node.next:
                corres[(node.next).val].append(node.next)
                heapq.heappush(min_heap, node.next.val)
        
        return head