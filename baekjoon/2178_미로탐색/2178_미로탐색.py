#34
from collections import deque

def bfs(mapp,visited):
    q = deque()
    q.append((0,0))
    visited[0][0] = 1

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    while q:
        cx, cy = q.popleft()
        if cx == N-1 and cy == M-1:
            return visited[cx][cy]
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and mapp[nx][ny] == '1' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[cx][cy] + 1 
                q.append((nx,ny))

    return

        
        
            



N, M = map(int,input().split())

mapp = []
visited = [[0] * M for _ in range(N)]

for i in range(N):
    mapp.append(input())

print(bfs(mapp,visited))