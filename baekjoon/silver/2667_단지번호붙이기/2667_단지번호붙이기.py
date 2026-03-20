#23
from collections import deque
def bfs(x,y,mapp,visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    cnt = 1
    
    while q:
        cx,cy = q.popleft()

        for i in range(4):
            nx = dx[i] + cx
            ny = dy[i] + cy
            if 0 <= nx < N and 0 <= ny < N and mapp[nx][ny] == '1' and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
                cnt += 1
    
    return cnt
                

            
N = int(input())
    

mapp = [input() for _ in range(N)]
visited = [[False] * N for _ in range(N)]
cnt = []

for i in range(N):
    for j in range(N):
        if mapp[i][j] == '1' and not visited[i][j]:
            cnt.append(bfs(i,j,mapp,visited))


print(len(cnt))

for i in sorted(cnt):
    print(i)

