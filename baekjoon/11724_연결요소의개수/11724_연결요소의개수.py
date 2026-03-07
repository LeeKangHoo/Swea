#14
import sys
sys.setrecursionlimit(10**6)
def dfs(start,mapp,visited):
    visited[start] = True
    for next in mapp[start]:
        if not visited[next]:
            dfs(next,mapp,visited)
            
input = sys.stdin.readline
N, M = map(int,input().split())
mapp = [[0] for _ in range(N+1)]
visited = [False] * (N+1)
r = []
cnt = 0
for i in range(M):
    v1, v2 = map(int,input().split())
    mapp[v1].append(v2)
    mapp[v2].append(v1)
for i in range(1,N+1):
    if not visited[i]:
        dfs(i,mapp,visited)
        cnt += 1
print(cnt)