#21
from collections import deque

def bfs(mapp,x,y):
    q = deque()
    q.append((x,y))
    mapp[x][y] = True
    c = 0

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not mapp[nx][ny]:
                mapp[nx][ny] = True
                q.append((nx,ny))
                c += 1
    return c + 1




M, N, K = map(int,input().split())

mapp = [[False]*N for _ in range(M)]
for i in range(K):
    x1, y1, x2, y2 = map(int,input().split())
    for a in range(y1,y2):
        for b in range(x1,x2):
            mapp[a][b] = True
cnt = 0
r = []
for i in range(M):
    for j in range(N):
        if not mapp[i][j]:
            r.append(bfs(mapp,i,j))
            cnt += 1
print(cnt)
print(*sorted(r))
