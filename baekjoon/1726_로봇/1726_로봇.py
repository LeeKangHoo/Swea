#X
from collections import deque
def bfs():
    q = deque()
    q.append(cur_idx)
    visited = [[[0] * 4 for _ in range(N)] for _ in range(M)]
    visited[cur_idx[0]][cur_idx[1]][cur_idx[2]] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        cx, cy, dir = q.popleft()

        if cx == target[0] and cy == target[1] and dir == target[2]:
            return visited[cx][cy][dir] - 1

        for k in range(1,4):
            nx = cx + dx[dir] * k
            ny = cy + dy[dir] * k

            if not(0 <= nx < M and 0 <= ny < N) or mapp[nx][ny] == '1':
                break

            if 0 <= nx < M and 0 <= ny < N and mapp[nx][ny] == '0' and visited[nx][ny][dir] == 0:
                visited[nx][ny][dir] = visited[cx][cy][dir] + 1
                q.append((nx,ny,dir))
        
        ######
        for i in range(4):
            if dir == i: continue

            if (dir < 2 and i < 2) or (dir >= 2 and i >= 2):
                turn_cnt = 2
            else:
                turn_cnt = 1
            
            if visited[cx][cy][i] == 0:
                visited[cx][cy][i] = visited[cx][cy][dir] + turn_cnt
                q.append((cx,cy,i))





M, N = map(int,input().split())
mapp = []
for i in range(M):
    mapp.append(list(input().split()))
cur_idx = list(map(int,input().split()))
target = list(map(int,input().split()))

for i in range(3):
    cur_idx[i] -= 1
    target[i] -= 1



print(bfs())