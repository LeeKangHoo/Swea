from collections import deque
#
def bfs(graph,visited,S,G):
    queue = deque()

    queue.append(S)
    

    while queue:
        cur = queue.popleft()
        if cur == G:
            return visited[G]
        for next in graph[cur]:
            if visited[next] == 0:
                queue.append(next)
                visited[next] += visited[cur] + 1
    return 0



T = int(input())



for i in range(T):
    V, E = map(int,input().split())

    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for j in range(E):
        v1 , v2 = map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    S, G = map(int, input().split())
    
    print(f"#{i+1} {bfs(graph,visited,S,G)}")