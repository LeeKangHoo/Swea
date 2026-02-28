#

def dfs(row,cur):
    
    global min_val

    if cur >= min_val:
        return
    
    if row == N:
        if cur < min_val:
            min_val = cur

    for next in range(N):
        if not visited[next]:
            visited[next] = True
            dfs(row+1, cur+graph[row][next])
            visited[next] = False
            

T = int(input())

for i in range(T):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    visited = [False] * N

    
    min_val = 9999

    dfs(0,0)

    print(f"#{i+1} {min_val}")

