/**
 * @param {number[][]} graph
 * @return {boolean}
 */
var isBipartite = function(graph) {
    let [group, visit, queue] = [new Array(graph.length).fill(-1), new Array(graph.length).fill(0), []];

    for(let i=0;i<graph.length;i++){
        if(!visit[i]){
            queue.push(i);
        }
        while(queue.length>0){
            let cur = queue.shift();
            visit[cur] = 1;

            if(group[cur]==-1){
                group[cur] = 0;
            }
            let near = (group[cur]+1)%2;

            for(adj of graph[cur]){
                if(group[adj]!=-1 && group[adj]!=near){
                    return false;
                }
                group[adj] = near;
                
                if(!visit[adj]){
                    queue.push(adj);
                }
            }
        }
    }
    return true;
};