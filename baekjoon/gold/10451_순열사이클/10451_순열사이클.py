#34
import sys
sys.setrecursionlimit(10**6)
def dfs(graph,visited,start):
    n = graph[start]
    if not visited[n]:
        visited[n] = True
        dfs(graph,visited,n)
        
    return

T = int(input())

for i in range(T):
    N = int(input())
    graph = [0] + list(map(int,input().split()))
    visited = [False] * (N+1)
    cnt = 0

    for next in range(1,N+1):
        if not visited[next]:
            dfs(graph,visited,next)
            cnt += 1

    print(cnt)

