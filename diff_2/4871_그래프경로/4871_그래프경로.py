#15
def dfs(S,G,graph,visited):
    visited.add(S)
    if S == G:
        return 1
    for i in graph[S]:
        if i not in visited:
            if dfs(i,G,graph,visited) == 1:
                return 1
    return 0


T = int(input())

for i in range(T):
    V,E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = set()
    for j in range(E):
        tmp1, tmp2 = map(int, input().split())
        graph[tmp1].append(tmp2)

    S,G = map(int, input().split())
    
    print(f"#{i+1} {dfs(S,G,graph,visited)}")