#7
from collections import deque

def bfs(graph,visited):
    q = deque()
    q.append(1)
    visited[1] = True

    while q:
        cur = q.popleft()

        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1) 

for i in range(M):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

bfs(graph,visited)

print(visited.count(True)-1)