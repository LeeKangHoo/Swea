#X
from collections import deque

def bfs(mapp,visited):
    q = deque()
    max_day = 0
    for i in range(N):
        for j in range(M):
            if mapp[i][j] == 1:
                q.append((i,j,0))
                visited[i][j] = True
            elif mapp[i][j] == -1:
                visited[i][j] = True
        

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while q:
        cx,cy,day_cnt = q.popleft()

        max_day = day_cnt

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and mapp[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx,ny,day_cnt+1))

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                return -1
    return max_day

        


M,N = map(int,input().split()) 
mapp = []
visited = [[False] * M for _ in range(N)]

for i in range(N):
    mapp.append(list(map(int,input().split())))


print(bfs(mapp,visited))