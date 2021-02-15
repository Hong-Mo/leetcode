"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        copy_first = Node(node.val, [])
        dic = {copy_first.val:[0, copy_first]}
        queue = [node]
        
        while queue:
            visit, copy_cur = queue.pop(0), None
            
            if visit.val not in dic.keys() :
                copy_cur = Node(visit.val, [])
                dic[visit.val] = [0, copy_cur]
            
            elif not dic[visit.val][0]:
                copy_cur = dic[visit.val][1]
            
            if copy_cur:
                for n_li in visit.neighbors:
                    if n_li.val not in dic.keys():
                        copy_n = Node(n_li.val, [])
                        dic[n_li.val] = [0, copy_n]
                    
                    else:
                        copy_n = dic[n_li.val][1]
                    
                    (copy_cur.neighbors).append(copy_n)
                    
                    if not dic[n_li.val][0]:
                        queue.append(n_li)
                
                dic[copy_cur.val][0] = 1
        
        return copy_first