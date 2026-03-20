#18
from collections import deque
def dfs(N,M,cur,visited,graph):
    visited.append(cur)
    print(cur,end=" ")
    for next in graph[cur]:
        if next not in visited:
            dfs(N,M,next,visited,graph)
    
    return
        



def bfs(N,M,cur,visited,graph):
    q = deque()
    q.append(cur)
    visited.append(cur)

    while q:
        c = q.popleft()
        print(c,end=" ")

        for next in graph[c]:
            if next not in visited:
                visited.append(next)
                q.append(next)


N, M, V = map(int,input().split())

dfs_visited = []
bfs_visited = []
dfs_graph = [[]for _ in range(N+1)]
bfs_graph = [[]for _ in range(N+1)]

for i in range(M):
    v1,v2 = map(int, input().split())
    dfs_graph[v1].append(v2)
    dfs_graph[v2].append(v1)
    bfs_graph[v1].append(v2)
    bfs_graph[v2].append(v1)

for i in range(N+1):
    dfs_graph[i] = sorted(dfs_graph[i])
    bfs_graph[i] = sorted(bfs_graph[i])
    

dfs(N,M,V,dfs_visited,dfs_graph)
print("")
bfs(N,M,V,bfs_visited,bfs_graph)
print("")