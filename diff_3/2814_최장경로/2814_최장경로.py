#14
def dfs(cur,graph,visited,dist):
    global max_val
    visited[cur] = True
    max_val = max(max_val, dist)

    for next in graph[cur]:
        if not visited[next]:
            dfs(next,graph,visited,dist+1)
            visited[next] = False
    
    return
            

T = int(input())

for i in range(T):
    N,M = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    for j in range(M):
        v1, v2 = map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    max_val = 0
    for z in range(1,N+1):
        dfs(z,graph,visited,1)
        visited[z] = False

    print(f"#{i+1} {max_val}")
    

