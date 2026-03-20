#X
from collections import deque

def bfs(mapp,visited):
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1
    dx = [-2,-1,1,2,2,1,-1,-2] 
    dy = [1,2,2,1,-1,-2,-2,-1]
    da = [-1,0,1,0]
    db = [0,1,0,-1]

    while q:
        cx, cy, moving_cnt = q.popleft()

        if cx == H-1 and cy == W-1:
            return visited[cx][cy][moving_cnt]-1

        if moving_cnt < K:
            for i in range(8):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < H and 0 <= ny < W and mapp[nx][ny] == 0 and visited[nx][ny][moving_cnt+1] == 0:
                    visited[nx][ny][moving_cnt+1] = visited[cx][cy][moving_cnt] + 1
                    q.append((nx,ny,moving_cnt+1))
        
        for i in range(4):
            nx = cx + da[i]
            ny = cy + db[i]
            if 0 <= nx < H and 0 <= ny < W and mapp[nx][ny] == 0 and visited[nx][ny][moving_cnt] == 0:
                visited[nx][ny][moving_cnt] = visited[cx][cy][moving_cnt] + 1
                q.append((nx,ny,moving_cnt))
        

    return -1



K = int(input())
W, H = map(int,input().split())

mapp = []
visited = [[[0] * (K+1) for _ in range(W)]for _ in range(H)]


for i in range(H):
    mapp.append(list(map(int,input().split())))

print(bfs(mapp,visited))
