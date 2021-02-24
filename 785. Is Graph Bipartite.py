class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        group, visit, queue = [-1]*len(graph), [0]*len(graph), []
        
        for i in range(len(graph)):
            if not visit[i]:
                queue.append(i)
            
            while queue:
                cur = queue.pop(0)
                visit[cur] = 1
                
                if group[cur]==-1:
                    group[cur] = 0
                
                near = (group[cur]+1)%2
                
                for adj in graph[cur]:
                    if group[adj]!=-1 and group[adj]!=near:
                        return False
                    
                    group[adj] = near
                    
                    if not visit[adj]:
                        queue.append(adj) 
        
        return True