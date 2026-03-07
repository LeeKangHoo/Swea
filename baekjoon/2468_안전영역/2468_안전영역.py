#33
from collections import deque
def bfs(x,y,mapp,visited,rain):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<= nx < N and 0 <= ny < N and mapp[nx][ny] > rain and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True




def solve(mapp):
    r = []
    max_val = 0
    for i in range(N):
        max_val = max(max_val,max(mapp[i]))
    for rain in range(max_val+1):
        visited = [[False] * N for _ in range(N)]
        cnt = 0
        for i in range(N):
            for j in range(N):
                if mapp[i][j] > rain and not visited[i][j]:
                    bfs(i,j,mapp,visited,rain)
                    cnt += 1
        r.append(cnt)
    return max(r)
    

N = int(input())

mapp = []

for i in range(N):
    mapp.append(list(map(int, input().split())))

print(solve(mapp))


