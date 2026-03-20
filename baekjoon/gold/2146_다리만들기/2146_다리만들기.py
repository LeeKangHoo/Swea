#X
from collections import deque
def find_bfs(x,y,mapp,visited):
    q = deque()
    q.append((x,y,island_cnt))
    visited[x][y] = 1
    mapp[x][y] = island_cnt

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    r = []

    while q:
        cx, cy, i_cnt = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                
                if mapp[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx,ny,i_cnt))
                    mapp[nx][ny] = island_cnt
                elif mapp[nx][ny] == 0:
                    r.append((nx,ny,i_cnt))
    return r
                    

def bridge_bfs(x,y,i_cnt,visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    while q:
        cx, cy = q.popleft()
        

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                if mapp[nx][ny] != i_cnt and mapp[nx][ny] != 0:
                    return visited[cx][cy]
                if mapp[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[cx][cy] + 1
                    q.append((nx,ny))

    return -1


N = int(input())
mapp = []
visited = [[0] * N for _ in range(N)]
island_cnt = 1

for i in range(N):
    mapp.append(list(map(int,input().split())))

s_point = set()
for i in range(N):
    if 1 in mapp[i]:
        for j in range(N):
            if not visited[i][j] and mapp[i][j] == 1:
                s_point.update(find_bfs(i,j,mapp,visited))
                island_cnt += 1

r = []
for i in s_point:
    visited_b = [[0] * N for _ in range(N)]
    dist = bridge_bfs(i[0],i[1],i[2],visited_b)
    if dist != -1:
        r.append(dist)

print(min(r))
